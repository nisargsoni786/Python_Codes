import google.oauth2.credentials
import google_auth_oauthlib.flow

flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
    'desk_creds.json',
    scopes=['https://www.googleapis.com/auth/drive.metadata.readonly'])

flow.redirect_uri = 'https://localhost:8080/oauth2callback'

authorization_url, state = flow.authorization_url(
    access_type='offline',
    include_granted_scopes='true')

print(authorization_url)