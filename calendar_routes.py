from fastapi import APIRouter, Request
from services.calendar_service import get_auth_url, exchange_code, get_events

router = APIRouter(prefix="/api/calendar", tags=["Calendar"])

@router.get("/auth-url")
def auth_url():
    return {"auth_url": get_auth_url()}

@router.get("/callback")
def callback(code: str):
    return exchange_code(code)

@router.get("/events")
async def events(access_token: str):
    return await get_events(access_token)