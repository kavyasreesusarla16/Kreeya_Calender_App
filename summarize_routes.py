from fastapi import APIRouter
from services.openai_service import summarize_text

router = APIRouter(prefix="/api/summarize", tags=["Summarize"])

@router.post("/")
async def summarize(payload: dict):
    text = payload.get("text", "")
    return await summarize_text(text)