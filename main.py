from googleapiclient.discovery import build
import json
from google.oauth2 import service_account
from datetime import datetime, timedelta
#TODO: Make sure that you create a file based on EXAMPLE_calendarsToSync and rename it
from config.helperFiles import calendarsToSync
import firebaseImport
from googleCalendar import googleCalendar
import functions_framework
from markupsafe import escape



@functions_framework.http

def sync_calendar(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        Returns a Success Message
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """

    request_json = request.get_json(silent=True)
    #TODO: Add ability to read arguments if you would like
    request_args = request.args

    #TODO: Ensure that Service Account JSON files are in /config/googleJSON, change the below 
    #      definition to that file name
    credentials_file = 'config/googleJSON/cloudServices.json'
    google_calendar = googleCalendar(credentials_file)
    google_calendar.authenticate()


    start_date = datetime.now()
    end_date = start_date + timedelta(days=21)
    event_list = []

    for c in calendarsToSync.calendarsToSync:
        print(c)
        events = google_calendar.get_events(c, start_date, end_date)
        
        for event in events:
            event_dict = {
                "id": event["id"],
                "calendar_id": c,
                "summary": event["summary"],
                "location": event.get('location', None),
                "description": event.get('description', None),
                "htmlLink": event["htmlLink"],
                "colorId": event.get('colorId', None),
                "start": event["start"],
                "end": event["end"]
            }
            event_list.append(event_dict)

    firebaseImport.import_json_to_firestore(event_list, 'events')

    return "Calendars Synced Correctly"

    


