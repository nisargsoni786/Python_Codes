import os
import requests
import datetime
from uuid import uuid4
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
import json,datetime

all_events = []


SCOPES = [
    "https://www.googleapis.com/auth/calendar",
    "https://www.googleapis.com/auth/calendar.readonly",
    "https://www.googleapis.com/auth/calendar.events",
    ]

def get_creds():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json',SCOPES)
        print("IS VALID >>>>> ",creds.valid)
        print("IS EXPIRED >>>>> ",creds.expired)
        # print(creds.refresh_token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('desk_creds.json',SCOPES)
            flow.redirect_uri = "http://localhost:8080/oauth2callback"
            creds = flow.run_local_server(port=0)

        with open ('token.json','w') as token:
            json_creds = creds.to_json()
            json_loads = json.loads(json_creds)
            json_loads["refresh_expiry"] = 300
            json_creds = json.dumps(json_loads)
            token.write(json_creds)

    return creds


if __name__ == '__main__':
    creds = get_creds()
    print(creds)
    service = build('calendar','v3',credentials=creds)

    ex_uuid = uuid4().hex
    print(ex_uuid,type(ex_uuid))

    # now = datetime.datetime.utcnow().isoformat() + 'Z'
    # events = service.events().list(calendarId='primary',singleEvents=True , orderBy='startTime').execute()
    # print("EVENTS   1\n",events)
    # all_events.append(events)
    # print("EVENTS   2\n",all_events)


    body = {
    'summary': 'Hello Felaassss',
    'location': 'Apna Adda',
    'description': 'Please attend the call...if u want to join Smart sense Solutions :)',
  'start': {
    'dateTime': '2021-10-29T09:00:00+00:00',
    'timeZone': 'Etc/UTC',
  },
  'end': {
    'dateTime': '2021-10-29T17:00:00+00:00',
    'timeZone': 'Etc/UTC',
  },
    'attendees': [
        {'email': 'nisarg.sict17@sot.pdpu.ac.in'},
        {'email': 'uttam.velani@smartsensesolutions.com'},
        {'email': 'krunal.chauhan@smartsensesolutions.com'},
    ],
    "conferenceData": {
        "createRequest" : {
            "requestId" : f"{uuid4().hex}"
        }
    },
    "reminders": {"useDefault": True}
    }

    event = service.events().insert(calendarId="primary", sendNotifications=True, body=body, conferenceDataVersion=1).execute()

    print(type(event))
    print(event)
