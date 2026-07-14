from fastapi import APIRouter
from pydantic import BaseModel
from app.services.router import route_prompt

router = APIRouter()

# Define what incoming data should look like
class ChatRequest(BaseModel):
    prompt: str
    model: str = "fast" # default value

@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    # Send the prompt and model choice to the orchestrator
    answer = await route_prompt(request.prompt, request.model)
    return {"response": answer}