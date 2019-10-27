from __future__ import print_function
import datetime
import time
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT
from backports.datetime_fromisoformat import MonkeyPatch

MonkeyPatch.patch_fromisoformat()
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def dayText(event):

    weekday = ['Mandag', 'Tirsdag', 'Onsdag', 'Torsdag', 'Fredag','Lørdag','Søndag']
    text = ''
    dt = datetime.datetime.fromisoformat(event['start'].get('dateTime', event['start'].get('date')))
    today = datetime.datetime.today()
    tomorrow = today + datetime.timedelta(1)

    if dt.date() == today.date() :
        text = text + 'I dag: '
    elif dt.date() == tomorrow.date() :
        text = text + 'I morgen: '
    else :
        text = text + weekday[dt.weekday()] + ': '

    text = text + event['summary']

    if dt.hour > 0:
        text = text + dt.strftime(' kl. %H:%M')

    return text

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '/home/pi/.creds.json', SCOPES)
            creds = flow.run_local_server()
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # create matrix device
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=8, block_orientation=90, rotate=0)
    print("Created device")

    start = time.perf_counter()
    while (start + 550) > time.perf_counter():
        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        # print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='parterapeutene.no_e1or90m2lp6p523ma7u15v2pc0@group.calendar.google.com', timeMin=now,
                                            maxResults=7, singleEvents=True,
                                            orderBy='startTime').execute()
        events = events_result.get('items', [])

        msg = ''

        if not events:
            msg = '- finner ingen middager - '
        for event in events:

            msg = dayText(event)
            show_message(device, msg, fill="white", font=proportional(CP437_FONT))
            time.sleep(2)

if __name__ == '__main__':
    main()
