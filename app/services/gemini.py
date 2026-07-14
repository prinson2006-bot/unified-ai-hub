from google.genai import Client, types
from app.core.config import settings

# Initialize the client with your API key
client = Client(api_key=settings.GEMINI_API_KEY).aio

# Global variable for memory
active_chat = None

# The secret sauce: Our specialized system instruction
ME_SYSTEM_PROMPT = """You are an expert Mechanical Engineering assistant. 
Your goal is to provide precise, technically accurate information regarding mechanical systems, thermodynamics, fluid mechanics, and materials science. 
When applicable, provide mathematical formulas, engineering standards, and practical considerations. 
You are also highly skilled in computational engineering — you should readily assist with Python scripts for CAD automation, data analysis, and numerical simulations.
Always use proper engineering terminology and keep responses analytical, structured, and practical. Do not use fluffy language."""

async def get_gemini_response(prompt: str, model_name: str = 'gemini-3.5-flash'):
    global active_chat
    
    # If no active chat, start one WITH the system instructions
    if active_chat is None:
        config = types.GenerateContentConfig(
            system_instruction=ME_SYSTEM_PROMPT,
        )
        active_chat = client.chats.create(model=model_name, config=config)
        
    # Send the prompt to the active session
    response = await active_chat.send_message(prompt)
    return response.text

def reset_chat_session():
    global active_chat
    active_chat = None