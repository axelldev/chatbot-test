from fastapi import APIRouter

from app.models import ChatRequest, ChatResponse
from app.services import add_message, get_conversation_history


router = APIRouter()


@router.get("/")
async def read_root():
    return {"message": "Chatbot API is running"}


@router.get("/health")
async def health():
    return {"status": "healthy"}


@router.post("/chat")
async def chat(request: ChatRequest):
    session_id = request.session_id
    add_message(session_id, "user", request.message)
    bot_response = "I'm a dummy response. OpenAI comming soon!"
    add_message(session_id, "assistant", bot_response)
    history = get_conversation_history(session_id)
    return ChatResponse(
        session_id=session_id,
        response=bot_response,
        message_count=len(history),
    )
