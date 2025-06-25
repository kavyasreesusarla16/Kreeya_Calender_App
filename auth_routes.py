from fastapi import APIRouter
from services.auth_service import login_supabase

router = APIRouter(prefix="/api/auth", tags=["Auth"])

@router.get("/login")
async def login(email: str, password: str):
    return await login_supabase(email, password)