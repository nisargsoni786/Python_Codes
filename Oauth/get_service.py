from googleapiclient.discovery import build
import json
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
import datetime
from db import get_db,init_db

init_db()
db = get_db()
Authorization = db["authorization"]

SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/calendar.readonly",
    "https://www.googleapis.com/auth/calendar.events",
    ]



def get_service():
    creds = None
    email = "nisarg.soni@smartsensesolutions.com"
    creds_db = Authorization.find_one({'email':email})
    print(creds_db)
    if creds_db:
        del creds_db["_id"]
        # creds = json.dumps(creds_db)
        creds = Credentials.from_authorized_user_info(creds_db,SCOPES)
        print(type(creds))

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('desk_creds.json',SCOPES)
            flow.redirect_uri = "http://localhost:8080/oauth2callback"
            creds = flow.run_local_server(port=0)
            print(type(creds))

            creds_json = json.loads(creds.to_json())
            creds_json["email"] = email
            creds_json["created_at"] = str(datetime.datetime.utcnow())

            Authorization.insert_one(creds_json)
    
    service = build('calendar','v3',credentials=creds)

    return service

