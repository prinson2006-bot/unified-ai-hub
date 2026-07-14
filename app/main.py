from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.services.router import router

app = FastAPI(title="Unified AI Hub")

# Allow the HTML frontend to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Attach our API routes
app.include_router(router, prefix="/api")