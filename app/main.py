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

# Target the index.html inside the frontend folder
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML_PATH = os.path.join(BASE_DIR, "frontend", "index.html")

@app.get("/")
async def serve_frontend():
    if os.path.exists(HTML_PATH):
        return FileResponse(HTML_PATH)
    return {"error": f"Looked for index.html at {HTML_PATH} but it wasn't there."}