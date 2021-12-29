@router_health.post("/google")
async def health_check_api(
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
        
        mime_type = resume.content_type
        file_name = resume.filename
        file_byte_obj = resume.file.read()
        
        print("FILE NAME>>>",file_name)
        print("MIME TYPE",mime_type)
        print("FILE",file_byte_obj)
        print("FILE OBJ TYPE",type(file_byte_obj))
        
        uuid1 = uuid4().hex

        message = MIMEMultipart()
        message["to"] = "nisargsoni786@gmail.com, nisarg.sict17@sot.pdpu.ac.in"
        message['cc'] = "nisargsoni654321@gmail.com, nayan.sakhiya@smartsensesolutions.com"
        message["from"] = "nisarg.soni@smartsensesolutions.com"
        message["subject"] = "JSNNNNNNNNNNNNNNNN"

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
