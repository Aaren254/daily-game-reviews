from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from oauth2client.client import OAuth2Credentials
import os

CLIENT_ID = os.environ["YOUTUBE_CLIENT_ID"]
CLIENT_SECRET = os.environ["YOUTUBE_CLIENT_SECRET"]
REFRESH_TOKEN = os.environ["YOUTUBE_REFRESH_TOKEN"]

def get_authenticated_service():
    credentials = OAuth2Credentials(
        access_token=None,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        refresh_token=REFRESH_TOKEN,
        token_expiry=None,
        token_uri="https://oauth2.googleapis.com/token",
        user_agent="my-user-agent/1.0",
    )
    return build("youtube", "v3", credentials=credentials)

def upload_video():
    youtube = get_authenticated_service()

    body = {
        "snippet": {
            "title": "Daily Game Review",
            "description": "Auto-generated daily review.",
            "tags": ["game", "review", "daily"],
            "categoryId": "20"  # Gaming
        },
        "status": {
            "privacyStatus": "public"
        }
    }

    media = MediaFileUpload("output.mp4", chunksize=-1, resumable=True)
    request = youtube.videos().insert(part="snippet,status", body=body, media_body=media)
    response = request.execute()
    print("Video uploaded:", response["id"])

if __name__ == "__main__":
    upload_video()

