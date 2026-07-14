from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.gemini import get_gemini_response, reset_chat_session

router = APIRouter()

class ChatRequest(BaseModel):
    prompt: str
    model: str = "fast"

@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        ai_text = await get_gemini_response(request.prompt, model_name="gemini-3.5-flash")
        return {"response": ai_text}
    except Exception as e:
        # If Gemini fails, send the error safely to the frontend
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/clear")
async def clear_chat():
    reset_chat_session()
    return {"status": "success", "message": "Memory wiped"}