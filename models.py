from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    email: str
    access_token: str
    refresh_token: str

class Event(BaseModel):
    summary: str
    start: str
    end: str
    description: Optional[str] = ""