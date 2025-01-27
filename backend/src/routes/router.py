from fastapi import APIRouter
from core.chat import chat
from pydantic import BaseModel

class ChatRequest(BaseModel):
    query: str

router = APIRouter()

@router.get("/health")
async def health_check():
    return {"status": "ok"}

@router.post("/chat")
async def chat_with_bot(request: ChatRequest):
    response = chat(request.query)
    return {"response": response}

# on-going
@router.post("/create_session", include_in_schema=False)
async def create_session():
    return {"message": "Creating a new session!"}

# on-going
@router.post("/upload_document", include_in_schema=False)
async def upload_document():
    return {"message": "Upload document in a session"}

