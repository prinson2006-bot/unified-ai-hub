from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class AIRequest(BaseModel):
    provider: str
    api_key: str
    prompt: str

@app.post("/ask")
def ask_ai(data: AIRequest):

    if data.provider == "gemini":
        url = (
            "https://generativelanguage.googleapis.com/v1beta/"
            f"models/gemini-1.5-flash:generateContent?key={data.api_key}"
        )

        payload = {
            "contents": [
                {"parts": [{"text": data.prompt}]}
            ]
        }

        response = requests.post(url, json=payload)
        return response.json()

    return {"error": "Provider not implemented"}
