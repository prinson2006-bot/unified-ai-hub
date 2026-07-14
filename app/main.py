import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from app.services.router import router

app = FastAPI(title="Unified AI Hub")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")

@app.get("/")
async def serve_frontend():
    # 1. Calculate possible directories
    current_dir = os.path.dirname(os.path.abspath(__file__)) # app/
    root_dir = os.path.dirname(current_dir) # project root
    
    # 2. List of paths to search for the frontend file
    possible_paths = [
        os.path.join(root_dir, "index.html"),
        os.path.join(current_dir, "index.html"),
        os.path.join(root_dir, "Index.html"),
        os.path.join(current_dir, "Index.html"),
    ]
    
    # 3. Search for the file
    for path in possible_paths:
        if os.path.exists(path):
            return FileResponse(path)
            
    # 4. If completely lost, print the directory mapping to the Render logs to debug
    print("\n--- CLOUD DIAGNOSTIC LOG ---")
    print(f"Current script folder (current_dir): {current_dir}")
    print(f"Contents of app folder: {os.listdir(current_dir) if os.path.exists(current_dir) else 'Not Found'}")
    print(f"Root project folder (root_dir): {root_dir}")
    print(f"Contents of root folder: {os.listdir(root_dir) if os.path.exists(root_dir) else 'Not Found'}")
    print("-----------------------------\n")
    
    return {"error": "index.html could not be found anywhere on the server. Check your Render logs for the directory map."}