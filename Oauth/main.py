from uuid import uuid4
import json,datetime
from get_service import get_service
from db import init_db

init_db()
uuid1 = uuid4().hex

service = get_service()

body = {
'summary': '2nd After db storage',
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
    # {'email': 'uttam.velani@smartsensesolutions.com'},
    # {'email': 'krunal.chauhan@smartsensesolutions.com'},
],
"conferenceData": {
    "createRequest" : {
        "requestId" : f"{uuid4().hex}"
    }
},
"reminders": {"useDefault": True}
}

event = service.events().insert(calendarId="primary", sendNotifications=True, body=body, conferenceDataVersion=1).execute()

# print(event)
print(f"\n\n\n----DONE----\n\n\n")