from googleapiclient.discovery import build
from google.oauth2 import service_account


class googleCalendar:
    def __init__(self, credentials_file):
        self.credentials_file = credentials_file
        self.service = None

    def authenticate(self):
        creds = service_account.Credentials.from_service_account_file(
            self.credentials_file, scopes=['https://www.googleapis.com/auth/calendar'])

        self.service = build('calendar', 'v3', credentials=creds)

    def get_events(self, calendar_id, start_date, end_date):
        start = start_date.isoformat() + 'Z'
        end = end_date.isoformat() + 'Z'

        events_result = self.service.events().list(
            calendarId=calendar_id,
            timeMin=start,
            timeMax=end,
            singleEvents=True,
            orderBy='startTime'
        ).execute()

        events = events_result.get('items', [])
        
        return events

   