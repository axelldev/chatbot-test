from fastapi import APIRouter

from app.models import ChatRequest, ChatResponse
from app.services import get_response


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
    response = get_response(session_id, request.message)
    return ChatResponse(
        session_id=session_id,
        response=response,
        message_count=0,
    )
