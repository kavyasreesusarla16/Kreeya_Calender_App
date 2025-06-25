import os
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
REDIRECT_URI = os.getenv("GOOGLE_REDIRECT_URI")
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]

def get_auth_url():
    flow = Flow.from_client_config({
        "web": {
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "redirect_uris": [REDIRECT_URI],
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token"
        }
    }, scopes=SCOPES)
    flow.redirect_uri = REDIRECT_URI
    auth_url, _ = flow.authorization_url(prompt="consent", access_type="offline")
    return auth_url

def exchange_code(code: str):
    flow = Flow.from_client_config({
        "web": {
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "redirect_uris": [REDIRECT_URI],
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token"
        }
    }, scopes=SCOPES)
    flow.redirect_uri = REDIRECT_URI
    flow.fetch_token(code=code)
    credentials = flow.credentials
    return {
        "access_token": credentials.token,
        "refresh_token": credentials.refresh_token
    }

async def get_events(access_token: str):
    creds = Credentials(token=access_token)
    service = build("calendar", "v3", credentials=creds)
    events_result = service.events().list(calendarId='primary', maxResults=5).execute()
    return events_result.get('items', [])