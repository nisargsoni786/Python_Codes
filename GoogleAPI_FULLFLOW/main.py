import google.oauth2.credentials
from google_auth_oauthlib import flow
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from starlette.responses import RedirectResponse
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
    "web_new_creds.json",
    scopes=[
        "https://www.googleapis.com/auth/calendar",
        "https://www.googleapis.com/auth/userinfo.profile",
        "https://www.googleapis.com/auth/userinfo.email",
    ],
)

flow.redirect_uri = "http://localhost"

authorization_url, state = flow.authorization_url(
    access_type="offline",
    login_hint="nisarg.soni@smartsensesolutions.com",
    include_granted_scopes="true",
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

# respp = requests.post(
#     "https://www.googleapis.com/oauth2/v3/tokeninfo",
#     params={"access_token": access_token},
# )
# print(respp)
# print(respp.json())


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
