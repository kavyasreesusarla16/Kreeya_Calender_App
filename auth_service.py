import httpx
import os

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_ANON_KEY")

async def login_supabase(email: str, password: str):
    url = f"{SUPABASE_URL}/auth/v1/token?grant_type=password"
    headers = {"apikey": SUPABASE_KEY, "Content-Type": "application/json"}
    data = {"email": email, "password": password}
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data, headers=headers)
        return response.json()