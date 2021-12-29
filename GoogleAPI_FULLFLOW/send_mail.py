from uuid import uuid4
import httplib2, base64
from email.mime.text import MIMEText


uuid1 = uuid4().hex

message = MIMEText("<h1>Hello there <b>Nisarg</b></h1>", "html")
message["Content-Type"] = "text/html"
message["to"] = "nisargsoni786@gmail.com"
message["from"] = "nisarg.soni@smartsensesolutions.com"
message["subject"] = "JSNNNNNNNNNNNNNNNN"


import google.oauth2.credentials

# from google_auth_oauthlib import flow
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
import requests, json
from urllib.parse import unquote

# Flow.from_client_config(
#     secrets_json_string,
#     scopes=[
#         (…),
#         'https://www.googleapis.com/auth/plus.me',
#     ],
#     redirect_uri=redirect_url
# )
# respp = requests.post(
#     "https://www.googleapis.com/oauth2/v3/tokeninfo",
#     params={"access_token": access_token},
# )
# print(respp)
# print(respp.json())

# ----------- IF WE DONT HAVE REFRESH TOKEN  -----------------

flow = Flow.from_client_secrets_file(
    "web_creds.json",
    scopes=[
        "https://www.googleapis.com/auth/calendar",
        "https://www.googleapis.com/auth/userinfo.profile",
        "https://www.googleapis.com/auth/userinfo.email",
        "https://www.googleapis.com/auth/gmail.send",
        "openid",
    ],
    redirect_uri="http://localhost/",
)


authorization_url, state = flow.authorization_url(
    access_type="offline",
    login_hint="nisarg.soni@smartsensesolutions.com",
    # include_granted_scopes="true",
    prompt="consent",
)

print(authorization_url)

code = input("\nEnter Code :- ")

# data = {
#     "client_id": "173840130101-utubvsioi12d9l8ni8f1orv3h37pv37h.apps.googleusercontent.com",
#     "client_secret": "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",
#     "redirect_uri": "http://localhost",
#     "grant_type": "authorization_code",
#     "code": unquote(unquote(code)),
# }

# resp = requests.post(
#     "https://oauth2.googleapis.com/token",
#     data=data,
#     headers={"content-type": "application/x-www-form-urlencoded"},
# )
# print(resp)
# resp_data = resp.json()
# print(resp_data)
# access_token = resp_data["access_token"]

flow.fetch_token(code=code)
creds = flow.credentials

creds_json = json.loads(creds.to_json())
print(creds_json)

respp = requests.post(
    "https://www.googleapis.com/oauth2/v3/tokeninfo",
    params={"access_token": creds_json["token"]},
)
print(respp)
print(respp.json())

# http = creds.authorize(httplib2.Http())

service = build("gmail", "v1", credentials=creds)

print("MESSAGE TYPE>>>", type(message), "\n\n")
print("MESSAGE>>>", message, "\n\n")
print("MESSAGE STR>>>", type(message.as_string()), "\n\n")
print("MESSAGE STR>>>", message.as_string(), "\n\n")

msg = (
    service.users()
    .messages()
    .send(
        userId="me",
        body={"raw": (base64.urlsafe_b64encode(message.as_bytes())).decode()},
    )
    .execute()
)

print(msg)


# ------------------- IF WE HAVE REFRESH TOKEN ----------------------

# data = {
#     "client_id": "173840130101-utubvsioi12d9l8ni8f1orv3h37pv37h.apps.googleusercontent.com",
#     "client_secret": "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",
#     "refresh_token": "1//0gcqrjpFnjQDwCgYIARAAGBASNwF-L9IrLEi3g7DJ9vm8Ph6f1Hqti3WGM46HZuYLendNZSs-JUxDM3b3YbSyRgg4_GVqcWD734M",
#     "grant_type": "refresh_token",
# }

# resp = requests.post(
#     "https://oauth2.googleapis.com/token",
#     data=data,
#     headers={"content-type": "application/x-www-form-urlencoded"},
# )
# print(resp)
# print(resp.json())
