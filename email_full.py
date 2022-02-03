from fastapi import APIRouter, Request, Response, UploadFile, File

from loguru import logger
from database.database import db_connection
from database.common_database import get_common_db
from helpers.response_helper import ResponseComposer
from constants import http_status_code

composerObj = ResponseComposer()
router_health = APIRouter(
    prefix="/health",
    tags=["Health"],
    responses={
        http_status_code.HTTP_OK: {"description": "Success"},
    },
    # dependencies=[Depends(HTTPBearer())],
)


@router_health.get("")
async def health_check_api(request: Request, response: Response):
    """
    API to check health of the project
    """
    try:
        conn = db_connection()
        if not conn:
            composerObj.make_response(
                message="Health Check Failed!",
                payload={"error": "MongoDB connection failed."},
                code=http_status_code.HTTP_BAD_REQUEST,
            )

        common_db_session = get_common_db()
        if common_db_session is None:
            return composerObj.make_response(
                message="Health Check Failed!",
                payload={"error": "CommanDB connection failed."},
                code=http_status_code.HTTP_BAD_REQUEST,
            )

        common_db_session.execute("SELECT 1")

        return composerObj.make_response(message="Health Check Successful!", code=http_status_code.HTTP_OK)
    except Exception as e:
        logger.exception(str(e))
        return composerObj.make_response(message="Health Check Failed!", code=http_status_code.HTTP_BAD_REQUEST)

    finally:
        common_db_session.close()


@router_health.post("")
async def GOOGLE(
    request: Request, 
    response: Response,
    resume: UploadFile = File(None),
    ):
    """
    API to check health of the project
    """
    try:
        from uuid import uuid4
        import httplib2, base64
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        from email.mime.base import MIMEBase
        from email import encoders
        
        from requests_oauthlib import OAuth2Session
        import requests
        
        mime_type = resume.content_type
        file_name = resume.filename
        file_byte_obj = resume.file.read()
        
        # print("FILE NAME>>>",file_name)
        # print("MIME TYPE",mime_type)
        # print("FILE",file_byte_obj)
        # print("FILE OBJ TYPE",type(file_byte_obj))
        
        uuid1 = uuid4().hex

        message = MIMEMultipart()
        message["to"] = "nisargsoni786@gmail.com, nisarg.sict17@sot.pdpu.ac.in"
        message['cc'] = "nisargsoni654321@gmail.com, nayan.sakhiya@smartsensesolutions.com"
        message["from"] = "nisarg.soni@smartsensesolutions.com"
        message["subject"] = "JSN GOOGLE"

        message.attach(MIMEText("<h1>Hello there <u>Nisarg</u></h1>", "html"))
        
        main_type = "application" 
        sub_type = "octet-stream"
        
        if mime_type:
            mime_type_split = mime_type.split('/',1)
            if len(mime_type_split)>1:
                main_type = mime_type_split[0]
                sub_type = mime_type_split[1]
        
        payload = MIMEBase(main_type, sub_type)
        payload.set_payload(file_byte_obj)
        encoders.encode_base64(payload)
        payload.add_header('content-disposition', 'attachment', filename=file_name)
        
        message.attach(payload)


        import google.oauth2.credentials

        # from google_auth_oauthlib import flow
        from googleapiclient.discovery import build
        from google_auth_oauthlib.flow import Flow
        from google.oauth2.credentials import Credentials
        from google.auth.transport.requests import Request
        import requests, json
        
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
        
        flow.fetch_token(code=code)
        creds = flow.credentials

        creds_json = json.loads(creds.to_json())

        respp = requests.post(
            "https://www.googleapis.com/oauth2/v3/tokeninfo",
            params={"access_token": creds_json["token"]},
        )


        # http = creds.authorize(httplib2.Http())

        service = build("gmail", "v1", credentials=creds)

        # print("MESSAGE TYPE>>>", type(message), "\n\n")
        # print("MESSAGE>>>", message, "\n\n")
        # print("MESSAGE STR>>>", type(message.as_string()), "\n\n")
        # print("MESSAGE STR>>>", message.as_string(), "\n\n")
        
        print(f"\n\n\n\n\n{type((base64.urlsafe_b64encode(message.as_bytes())).decode())}\n\n\n\n\n\n")
        print(f"\n\n\n\n\n{(base64.urlsafe_b64encode(message.as_bytes())).decode()}\n\n\n\n\n\n")

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

        return composerObj.make_response(message="CHECKKK", code=http_status_code.HTTP_OK)
    except Exception as e:
        logger.exception(str(e))
        return composerObj.make_response(message="Health Check Failed!", code=http_status_code.HTTP_BAD_REQUEST)



@router_health.put("")
async def MS_JSON(
    request: Request, 
    response: Response,
    resume: UploadFile = File(None),
    ):
    """
    API to check health of the project
    """
    try:
        import base64,json
        
        mime_type = resume.content_type
        file_name = resume.filename
        file_byte_obj = resume.file.read()
        body={
        "message": {
            "subject": "Meet for lunch?",
            "body": {
            "contentType": "HTML",
            "content": "The new cafeteria is open.<h1>JSN</h1>"
            },
            "toRecipients": [
            {
                "emailAddress": {
                "address": "nisargsoni786@gmail.com"
                }
            }
            ],
            "attachments":[
                {
                "@odata.type": "#microsoft.graph.fileAttachment",
                "name": file_name,
                "contentType": mime_type,
                "contentBytes": base64.b64encode(file_byte_obj).decode('utf-8')
                }
            ]
        },
        "saveToSentItems": "true"
        }

        from requests_oauthlib import OAuth2Session
        import requests

        client_id = "9b5b4a13d-af971163c075"
        # client_secret = "f5bc31e-b297-d63d5afc83ca"
        client_secret = "iSd7Q~skeVpNmWxi6xgE5wZdD_QGBqOVd3Y"
        sec_id = "f2892aa2-315c-48bb-a8-7f15003e425b"

        redirect_uri = "http://localhost"
        TOKEN_ENDPOINT = '/oauth2/v2.0/token'

        SCOPES = [
            'Calendars.ReadWrite',
            'offline_access',
            'Mail.ReadWrite',
            'Mail.Send',
            'openid',
            'profile',
            'User.Read',
            'openid',
            'profile',
            'offline_access',
            'email'
        ]

        client = OAuth2Session(client_id,
                                redirect_uri=redirect_uri,
                                scope=SCOPES)

        authorization_url,state = client.authorization_url(
            "https://login.microsoftonline.com/common/oauth2/v2.0/authorize",
            )

        print(authorization_url)

        code = input("\nEnter Code :- ")

        token = client.fetch_token("https://login.microsoftonline.com/common/oauth2/v2.0/token",
                                    client_secret=client_secret,
                                    code=code,
                                    client_id=client_id,
                                    state=state)

        request_headers = {'Authorization': 'bearer %s'%(token['access_token']) , "Content-Type": "application/json"}


        graph_client = OAuth2Session(token=token)
        resp = graph_client.post("https://graph.microsoft.com/v1.0/me/sendMail",data=json.dumps(body),headers=request_headers)
        print(resp)
        print(resp.text)


        return composerObj.make_response(message="CHECKKK", code=http_status_code.HTTP_OK)
    except Exception as e:
        logger.exception(str(e))
        return composerObj.make_response(message="Health Check Failed!", code=http_status_code.HTTP_BAD_REQUEST)



@router_health.delete("")
async def MS_MIME(
    request: Request, 
    response: Response,
    resume: UploadFile = File(None),
    ):
    """
    API to check health of the project
    """
    try:
        from requests_oauthlib import OAuth2Session
        import requests
        from uuid import uuid4
        import httplib2, base64
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart
        from email.mime.base import MIMEBase
        from email import encoders
        
        mime_type = resume.content_type
        file_name = resume.filename
        file_byte_obj = resume.file.read()
        
        # print("FILE NAME>>>",file_name)
        # print("MIME TYPE",mime_type)
        # print("FILE",file_byte_obj)
        # print("FILE OBJ TYPE",type(file_byte_obj))
        
        uuid1 = uuid4().hex

        message = MIMEMultipart()
        message["to"] = "nisargsoni786@gmail.com, nisarg.sict17@sot.pdpu.ac.in"
        message['cc'] = "nisargsoni654321@gmail.com, nayan.sakhiya@smartsensesolutions.com"
        message["from"] = "nisarg.soni@smartsensesolutions.com"
        message["subject"] = "MSSSS_JSOn"

        message.attach(MIMEText("<h1>Hello there <u>Nisarg</u></h1>", "html"))
        
        main_type = "application" 
        sub_type = "octet-stream"
        
        if mime_type:
            mime_type_split = mime_type.split('/',1)
            if len(mime_type_split)>1:
                main_type = mime_type_split[0]
                sub_type = mime_type_split[1]
        
        payload = MIMEBase(main_type, sub_type)
        payload.set_payload(file_byte_obj)
        encoders.encode_base64(payload)
        payload.add_header('content-disposition', 'attachment', filename=file_name)
        
        message.attach(payload)

        client_id = "9b5b4b7c-d855-42a13d-af971163c075"
        client_secret = "iSd7Q~sVpNmWxoxi6xgE5wZdD_QGBqOVd3Y"
        sec_id = "f2892aa2-31-48bb-a86e-7f15003e425b"

        redirect_uri = "http://localhost"
        TOKEN_ENDPOINT = '/oauth2/v2.0/token'

        SCOPES = [
            'Calendars.ReadWrite',
            'offline_access',
            'Mail.ReadWrite',
            'Mail.Send',
            'openid',
            'profile',
            'User.Read',
            'openid',
            'profile',
            'offline_access',
            'email'
        ]

        client = OAuth2Session(client_id,
                                redirect_uri=redirect_uri,
                                scope=SCOPES)

        authorization_url,state = client.authorization_url(
            "https://login.microsoftonline.com/common/oauth2/v2.0/authorize",
            )

        print(authorization_url)

        code = input("\nEnter Code :- ")

        token = client.fetch_token("https://login.microsoftonline.com/common/oauth2/v2.0/token",
                                    client_secret=client_secret,
                                    code=code,
                                    client_id=client_id,
                                    state=state)

        request_headers = {'Authorization': 'bearer %s'%(token['access_token']) , "Content-Type": "text/plain"}

        print(f"\n\n\n\n\n{type((base64.urlsafe_b64encode(message.as_bytes())).decode())}\n\n\n\n\n\n")
        print(f"\n\n\n\n\n{(base64.urlsafe_b64encode(message.as_bytes())).decode()}\n\n\n\n\n\n")

        graph_client = OAuth2Session(token=token)
        resp = graph_client.post("https://graph.microsoft.com/v1.0/me/sendMail",data=base64.urlsafe_b64encode(message.as_bytes()).decode(),headers=request_headers)
        print(resp)
        print(resp.text)


        return composerObj.make_response(message="CHECKKK", code=http_status_code.HTTP_OK)
    except Exception as e:
        logger.exception(str(e))
        return composerObj.make_response(message="Health Check Failed!", code=http_status_code.HTTP_BAD_REQUEST)

