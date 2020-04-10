from google.oauth2 import service_account

CREDENTIALS = None
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def get_creds():
  global CREDENTIALS
  if CREDENTIALS is None:
    CREDENTIALS = service_account.Credentials.from_service_account_file('secret/credentials.json', scopes=SCOPES)
  return CREDENTIALS
