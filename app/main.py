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

# NEW: Serve the frontend HTML file at the root URL
@app.get("/")
async def serve_frontend():
    return FileResponse("index.html")