Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from os import chdir
chdir(r"C:\Users\ignsz\Desktop\calendar_API")
exec("""from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
""")
exec("""creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())""")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    exec("""creds = None
  File "<string>", line 5
    if os.path.exists('token.json'):
IndentationError: unexpected indent
exec("""creds = None
    if True:
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())""")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    exec("""creds = None
  File "<string>", line 2
    if True:
IndentationError: unexpected indent
exec("""creds = None
if True:
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())""")
         
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    exec("""creds = None
  File "<string>", line 14, in <module>
NameError: name 'SCOPES' is not defined
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


======================= RESTART: Shell =======================
from os import chdir
chdir(r"C:\Users\ignsz\Desktop\calendar_API")
exec("""from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
""")
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
SCOPES = ['https://www.googleapis.com/auth/calendar.modify']
exec("""creds = None
if True:
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())""")
Please visit this URL to authorize this application: https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=825295090122-94nvga9hp2916jhehdt0vge6pca4n01m.apps.googleusercontent.com&redirect_uri=http%3A%2F%2Flocalhost%3A53839%2F&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcalendar.modify&state=ViwWwRSBWQLj3qcFestEd3sn7IVo5q&access_type=offline

======================= RESTART: Shell =======================
SCOPES = ['https://www.googleapis.com/auth/calendar']

from os import chdir
chdir(r"C:\Users\ignsz\Desktop\calendar_API")
exec("""from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
""")
exec("""creds = None
if True:
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())""")
Please visit this URL to authorize this application: https://accounts.google.com/o/oauth2/auth?response_type=code&client_id=825295090122-94nvga9hp2916jhehdt0vge6pca4n01m.apps.googleusercontent.com&redirect_uri=http%3A%2F%2Flocalhost%3A53877%2F&scope=https%3A%2F%2Fwww.googleapis.com%2Fauth%2Fcalendar&state=WgGNxSlgbTTPLIruukY5ZoBTv8nfbz&access_type=offline
calendar = {
    'summary': 'PersonsDays',
    'timeZone': 'Europe/Warsaw'
}
created_calendar = service.calendars().insert(body=calendar).execute()
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    created_calendar = service.calendars().insert(body=calendar).execute()
NameError: name 'service' is not defined
service = build('calendar', 'v3', credentials=creds)
created_calendar = service.calendars().insert(body=calendar).execute()
created_calendar['id']

'16s1c8l6ull2t5se6r4uno73u0@group.calendar.google.com'
cal_id = _
{
  "kind": "calendar#event",
  "etag": etag,
  "id": string,
  "status": string,
  "htmlLink": string,
  "created": datetime,
  "updated": datetime,
  "summary": string,
  "description": string,
  "location": string,
  "colorId": string,
  "creator": {
    "id": string,
    "email": string,
    "displayName": string,
    "self": boolean
  },
  "organizer": {
    "id": string,
    "email": string,
    "displayName": string,
    "self": boolean
  },
  "start": {
    "date": date,
    "dateTime": datetime,
    "timeZone": string
  },
  "end": {
    "date": date,
    "dateTime": datetime,
    "timeZone": string
  },
  "endTimeUnspecified": boolean,
  "recurrence": [
    string
  ],
  "recurringEventId": string,
  "originalStartTime": {
    "date": date,
    "dateTime": datetime,
    "timeZone": string
  },
  "transparency": string,
  "visibility": string,
  "iCalUID": string,
  "sequence": integer,
  "attendees": [
    {
      "id": string,
      "email": string,
      "displayName": string,
      "organizer": boolean,
      "self": boolean,
      "resource": boolean,
      "optional": boolean,
      "responseStatus": string,
      "comment": string,
      "additionalGuests": integer
    }
  ],
  "attendeesOmitted": boolean,
  "extendedProperties": {
    "private": {
      (key): string
    },
    "shared": {
      (key): string
    }
  },
  "hangoutLink": string,
  "conferenceData": {
    "createRequest": {
      "requestId": string,
      "conferenceSolutionKey": {
        "type": string
      },
      "status": {
        "statusCode": string
      }
    },
    "entryPoints": [
      {
        "entryPointType": string,
        "uri": string,
        "label": string,
        "pin": string,
        "accessCode": string,
        "meetingCode": string,
        "passcode": string,
        "password": string
      }
    ],
    "conferenceSolution": {
      "key": {
        "type": string
      },
      "name": string,
      "iconUri": string
    },
    "conferenceId": string,
    "signature": string,
    "notes": string,
  },
  "gadget": {
    "type": string,
    "title": string,
    "link": string,
    "iconLink": string,
    "width": integer,
    "height": integer,
    "display": string,
    "preferences": {
      (key): string
    }
  },
  "anyoneCanAddSelf": boolean,
  "guestsCanInviteOthers": boolean,
  "guestsCanModify": boolean,
  "guestsCanSeeOtherGuests": boolean,
  "privateCopy": boolean,
  "locked": boolean,
  "reminders": {
    "useDefault": boolean,
    "overrides": [
      {
        "method": string,
        "minutes": integer
      }
    ]
  },
  "source": {
    "url": string,
    "title": string
  },
  "attachments": [
    {
      "fileUrl": string,
      "title": string,
      "mimeType": string,
      "iconLink": string,
      "fileId": string
    }
  ],
  "eventType": string
}
Traceback (most recent call last):
  File "<pyshell#33>", line 3, in <module>
    "etag": etag,
NameError: name 'etag' is not defined
event = {
  'summary': 'TEST',
  'start': {
    'dateTime': '2022-07-12T10:00:00.000-07:00',
    'timeZone': 'Europe/Warsaw'
  },
  'end': {
    'dateTime': '2022-07-12T10:00:00.000-08:00',,
    'timeZone': 'Europe/Warsaw'
  },
  'recurrence': [
    'RRULE:FREQ=YEARLY',
  ]
}

SyntaxError: expression expected after dictionary key and ':'
event = {
  'summary': 'TEST',
  'start': {
    'dateTime': '2022-07-12T10:00:00.000-07:00',
    'timeZone': 'Europe/Warsaw'
  },
  'end': {
    'dateTime': '2022-07-12T10:00:00.000-08:00',
    'timeZone': 'Europe/Warsaw'
  },
  'recurrence': [
    'RRULE:FREQ=YEARLY',
  ]
}
recurring_event = service.events().insert(calendarId=cal_id, body=event).execute()

Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    recurring_event = service.events().insert(calendarId=cal_id, body=event).execute()
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\googleapiclient\_helpers.py", line 130, in positional_wrapper
    return wrapped(*args, **kwargs)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\googleapiclient\http.py", line 923, in execute
    resp, content = _retry_request(
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\googleapiclient\http.py", line 222, in _retry_request
    raise exception
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\googleapiclient\http.py", line 191, in _retry_request
    resp, content = http.request(uri, method, *args, **kwargs)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\google_auth_httplib2.py", line 218, in request
    response, content = self.http.request(
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\httplib2\__init__.py", line 1701, in request
    (response, content) = self._request(
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\httplib2\__init__.py", line 1421, in _request
    (response, content) = self._conn_request(conn, request_uri, method, body, headers)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\httplib2\__init__.py", line 1344, in _conn_request
    conn.request(method, request_uri, body, headers)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 992, in send
    self.sock.sendall(data)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\ssl.py", line 1236, in sendall
    v = self.send(byte_view[count:])
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\ssl.py", line 1205, in send
    return self._sslobj.write(data)
ssl.SSLEOFError: EOF occurred in violation of protocol (_ssl.c:2384)
recurring_event = service.events().insert(calendarId=cal_id, body=event).execute()
event = {
  'summary': 'TEST',
  'start': {
    'dateTime': '2022-07-12',
    'timeZone': 'Europe/Warsaw'
  },
  'end': {
    'dateTime': '2022-07-12',
    'timeZone': 'Europe/Warsaw'
  },
}

recurring_event = service.events().insert(calendarId=cal_id, body=event).execute()
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    recurring_event = service.events().insert(calendarId=cal_id, body=event).execute()
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\googleapiclient\_helpers.py", line 130, in positional_wrapper
    return wrapped(*args, **kwargs)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\googleapiclient\http.py", line 938, in execute
    raise HttpError(resp, content, uri=self.uri)
googleapiclient.errors.HttpError: <HttpError 400 when requesting https://www.googleapis.com/calendar/v3/calendars/16s1c8l6ull2t5se6r4uno73u0%40group.calendar.google.com/events?alt=json returned "Bad Request". Details: "[{'domain': 'global', 'reason': 'badRequest', 'message': 'Bad Request'}]">
recurring_event = service.events().insert(calendarId=cal_id, body=event).execute()
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    recurring_event = service.events().insert(calendarId=cal_id, body=event).execute()
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\googleapiclient\_helpers.py", line 130, in positional_wrapper
    return wrapped(*args, **kwargs)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\googleapiclient\http.py", line 938, in execute
    raise HttpError(resp, content, uri=self.uri)
googleapiclient.errors.HttpError: <HttpError 400 when requesting https://www.googleapis.com/calendar/v3/calendars/16s1c8l6ull2t5se6r4uno73u0%40group.calendar.google.com/events?alt=json returned "Bad Request". Details: "[{'domain': 'global', 'reason': 'badRequest', 'message': 'Bad Request'}]">
event = {
  'summary': 'TEST',
  'start': {
    'dateTime': '2022-07-12',
    'timeZone': 'Europe/Warsaw'
  },
  'end': {
    'dateTime': '2022-07-12',
    'timeZone': 'Europe/Warsaw'
  }
}
recurring_event = service.events().insert(calendarId=cal_id, body=event).execute()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    recurring_event = service.events().insert(calendarId=cal_id, body=event).execute()
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\googleapiclient\_helpers.py", line 130, in positional_wrapper
    return wrapped(*args, **kwargs)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\googleapiclient\http.py", line 938, in execute
    raise HttpError(resp, content, uri=self.uri)
googleapiclient.errors.HttpError: <HttpError 400 when requesting https://www.googleapis.com/calendar/v3/calendars/16s1c8l6ull2t5se6r4uno73u0%40group.calendar.google.com/events?alt=json returned "Bad Request". Details: "[{'domain': 'global', 'reason': 'badRequest', 'message': 'Bad Request'}]">
event = {
  'summary': 'TEST',
  'start': {
    'date': '2022-07-12',
    'timeZone': 'Europe/Warsaw'
  },
  'end': {
    'date': '2022-07-12',
    'timeZone': 'Europe/Warsaw'
  }
}
recurring_event = service.events().insert(calendarId=cal_id, body=event).execute()
from pickle import load
file = open("persons.bin",'wb')
data = load(file)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    data = load(file)
io.UnsupportedOperation: read
file = open("persons.bin",'rb')
data = load(file)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    data = load(file)
EOFError: Ran out of input
file.close()
file = open("persons.bin",'wb')
file.close()
file = open("persons.bin",'r')
data = load(file)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    data = load(file)
TypeError: a bytes-like object is required, not 'str'
file.close()
file = open("persons.bin",'rb')
data = load(file)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    data = load(file)
EOFError: Ran out of input
file.close()
file = open("persons.bin",'rb')
data = load(file)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    data = load(file)
AttributeError: Can't get attribute 'Person' on <module '__main__' (built-in)>
from collections import namedtuple
Person = namedtuple("Person", ["Name", "birtshday", "namesday"])
Date = namedtuple("Date", ["Day", "Month"])
data = load(file)
data

def create_event(name, day, month):  
    event = {
    'summary': 'TEST',
    'start': {
        'date': f'2022-{month}-{day}',
        'timeZone': 'Europe/Warsaw'
    },
    'end': {
        'date': f'2022-{month}-{day}',
        'timeZone': 'Europe/Warsaw'
    },
    'recurrence': [
    'RRULE:FREQ=YEARLY',
    ]
    
}

    
for person in data:
    name, bd, nd = person
    if bd is not None:
        bdd, bdm = bd
        ev_name = "URODZINY: " + name
        ev = create_event(ev_name, bdd,bdm)
        service.events().insert(calendarId=cal_id, body=event).execute()
        if nd is not None:
        bdd, bdm = nd
        ev_name = "IMIENINY: " + name
        ev = create_event(ev_name, bdd,bdm)
        service.events().insert(calendarId=cal_id, body=event).execute()

SyntaxError: expected an indented block after 'if' statement on line 8
for person in data:
    name, bd, nd = person
    if bd is not None:
        bdd, bdm = bd
        ev_name = "URODZINY: " + name
        ev = create_event(ev_name, bdd,bdm)
        service.events().insert(calendarId=cal_id, body=event).execute()
    if nd is not None:
        bdd, bdm = nd
        ev_name = "IMIENINY: " + name
        ev = create_event(ev_name, bdd,bdm)
        service.events().insert(calendarId=cal_id, body=event).execute()

        
Traceback (most recent call last):
  File "<pyshell#81>", line 7, in <module>
    service.events().insert(calendarId=cal_id, body=event).execute()
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\googleapiclient\_helpers.py", line 130, in positional_wrapper
    return wrapped(*args, **kwargs)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\googleapiclient\http.py", line 923, in execute
    resp, content = _retry_request(
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\googleapiclient\http.py", line 222, in _retry_request
    raise exception
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\googleapiclient\http.py", line 191, in _retry_request
    resp, content = http.request(uri, method, *args, **kwargs)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\google_auth_httplib2.py", line 218, in request
    response, content = self.http.request(
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\httplib2\__init__.py", line 1701, in request
    (response, content) = self._request(
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\httplib2\__init__.py", line 1421, in _request
    (response, content) = self._conn_request(conn, request_uri, method, body, headers)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\httplib2\__init__.py", line 1344, in _conn_request
    conn.request(method, request_uri, body, headers)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 992, in send
    self.sock.sendall(data)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\ssl.py", line 1236, in sendall
    v = self.send(byte_view[count:])
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\ssl.py", line 1205, in send
    return self._sslobj.write(data)
ssl.SSLEOFError: EOF occurred in violation of protocol (_ssl.c:2384)
for person in data:
    name, bd, nd = person
    if bd is not None:
        bdd, bdm = bd
        ev_name = "URODZINY: " + name
        ev = create_event(ev_name, bdd,bdm)
        service.events().insert(calendarId=cal_id, body=event).execute()
    if nd is not None:
        bdd, bdm = nd
        ev_name = "IMIENINY: " + name
        ev = create_event(ev_name, bdd,bdm)
        service.events().insert(calendarId=cal_id, body=event).execute()

        

for person in data:
    name, bd, nd = person
    if bd is not None:
        bdd, bdm = bd
        ev_name = "URODZINY: " + name
        ev = create_event(ev_name, bdd,bdm)
        _ = service.events().insert(calendarId=cal_id, body=ev).execute()
    if nd is not None:
        bdd, bdm = nd
        ev_name = "IMIENINY: " + name
        ev = create_event(ev_name, bdd,bdm)
        _ = service.events().insert(calendarId=cal_id, body=ev).execute()

        
Traceback (most recent call last):
  File "<pyshell#85>", line 7, in <module>
    _ = service.events().insert(calendarId=cal_id, body=ev).execute()
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\googleapiclient\_helpers.py", line 130, in positional_wrapper
    return wrapped(*args, **kwargs)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\googleapiclient\http.py", line 938, in execute
    raise HttpError(resp, content, uri=self.uri)
googleapiclient.errors.HttpError: <HttpError 400 when requesting https://www.googleapis.com/calendar/v3/calendars/16s1c8l6ull2t5se6r4uno73u0%40group.calendar.google.com/events?alt=json returned "Missing end time.". Details: "[{'domain': 'global', 'reason': 'required', 'message': 'Missing end time.'}]">
for person in data:
    name, bd, nd = person
    if bd is not None:
        bdd, bdm = bd
        ev_name = "URODZINY: " + name
        ev = create_event(ev_name, bdd,bdm)
        print(bd, ev)
        #_ = service.events().insert(calendarId=cal_id, body=ev).execute()
    if nd is not 
        bdd, bdm = nd
        ev_name = "IMIENINY: " + name
        ev = create_event(ev_name, bdd,bdm)
        print(nd, ev)
        #_ = service.events().insert(calendarId=cal_id, body=ev).execute()
        
SyntaxError: invalid syntax
for person in data:
    name, bd, nd = person
    if bd is not None:
        bdd, bdm = bd
        ev_name = "URODZINY: " + name
        ev = create_event(ev_name, bdd,bdm)
        print(bd, ev)
        #_ = service.events().insert(calendarId=cal_id, body=ev).execute()
    if nd is not None:
        bdd, bdm = nd
        ev_name = "IMIENINY: " + name
        ev = create_event(ev_name, bdd,bdm)
        print(nd, ev)
        #_ = service.events().insert(calendarId=cal_id, body=ev).execute()

        

def create_event(name, day, month):
    event = {
    'summary': 'TEST',
    'start': {
        'date': f'2022-{month}-{day}',
        'timeZone': 'Europe/Warsaw'
    },
    'end': {
        'date': f'2022-{month}-{day}',
        'timeZone': 'Europe/Warsaw'
    },
    'recurrence': [
    'RRULE:FREQ=YEARLY',
    ]

    }
    return event

def create_event(name, day, month):
    event = {
    'summary': 'TEST',
    'start': {
        'date': f'2022-{month}-{day}',
        'timeZone': 'Europe/Warsaw'
    },
    'end': {
        'date': f'2022-{month}-{day}',
        'timeZone': 'Europe/Warsaw'
    },
    'recurrence': [
    'RRULE:FREQ=YEARLY',
    ]

    }
    return event

for person in data:
    name, bd, nd = person
    if bd is not None:
        bdd, bdm = bd
        ev_name = "URODZINY: " + name
        ev = create_event(ev_name, bdd,bdm)
        print(bd, ev)
        #_ = service.events().insert(calendarId=cal_id, body=ev).execute()
    if nd is not None:
        bdd, bdm = nd
        ev_name = "IMIENINY: " + name
        ev = create_event(ev_name, bdd,bdm)
        print(nd, ev)
        #_ = service.events().insert(calendarId=cal_id, body=ev).execute()

        

for person in data:
    name, bd, nd = person
    if bd is not None:
        bdd, bdm = bd
        ev_name = "URODZINY: " + name
        ev = create_event(ev_name, bdd,bdm)
        _ = service.events().insert(calendarId=cal_id, body=ev).execute()
    if nd is not None:
        bdd, bdm = nd
        ev_name = "IMIENINY: " + name
        ev = create_event(ev_name, bdd,bdm)
        _ = service.events().insert(calendarId=cal_id, body=ev).execute()

  
Traceback (most recent call last):
  File "<pyshell#98>", line 7, in <module>
    _ = service.events().insert(calendarId=cal_id, body=ev).execute()
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\googleapiclient\_helpers.py", line 130, in positional_wrapper
    return wrapped(*args, **kwargs)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\googleapiclient\http.py", line 923, in execute
    resp, content = _retry_request(
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\googleapiclient\http.py", line 222, in _retry_request
    raise exception
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\googleapiclient\http.py", line 191, in _retry_request
    resp, content = http.request(uri, method, *args, **kwargs)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\google_auth_httplib2.py", line 218, in request
    response, content = self.http.request(
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\httplib2\__init__.py", line 1701, in request
    (response, content) = self._request(
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\httplib2\__init__.py", line 1421, in _request
    (response, content) = self._conn_request(conn, request_uri, method, body, headers)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\httplib2\__init__.py", line 1344, in _conn_request
    conn.request(method, request_uri, body, headers)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 992, in send
    self.sock.sendall(data)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\ssl.py", line 1236, in sendall
    v = self.send(byte_view[count:])
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\ssl.py", line 1205, in send
    return self._sslobj.write(data)
ssl.SSLEOFError: EOF occurred in violation of protocol (_ssl.c:2384)
for person in data:
    name, bd, nd = person
    if bd is not None:
        bdd, bdm = bd
        ev_name = "URODZINY: " + name
        ev = create_event(ev_name, bdd,bdm)
        _ = service.events().insert(calendarId=cal_id, body=ev).execute()
    if nd is not None:
        bdd, bdm = nd
        ev_name = "IMIENINY: " + name
        ev = create_event(ev_name, bdd,bdm)
        _ = service.events().insert(calendarId=cal_id, body=ev).execute()

  

def create_event(name, day, month):
    event = {
    'summary': f'name',
    'start': {
        'date': f'2022-{month}-{day}',
        'timeZone': 'Europe/Warsaw'
    },
    'end': {
        'date': f'2022-{month}-{day}',
        'timeZone': 'Europe/Warsaw'
    },
    'recurrence': [
    'RRULE:FREQ=YEARLY',
    ]

    }
    return event

  
calendar = {
    'summary': 'PersonsDays',
    'timeZone': 'Europe/Warsaw'
}
  
created_calendar = service.calendars().insert(body=calendar).execute()
  
cal_id = created_calendar["id"]
  
cal_id
  
'bnec7up2q3uo5m6a203spm3a9k@group.calendar.google.com'
for person in data:
    name, bd, nd = person
    if bd is not None:
        bdd, bdm = bd
        ev_name = "URODZINY: " + name
        ev = create_event(ev_name, bdd,bdm)
        _ = service.events().insert(calendarId=cal_id, body=ev).execute()
    if nd is not None:
        bdd, bdm = nd
        ev_name = "IMIENINY: " + name
        ev = create_event(ev_name, bdd,bdm)
        _ = service.events().insert(calendarId=cal_id, body=ev).execute()

  
def create_event(name, day, month):
    event = {
    'summary': f'name',
    'start': {
        'date': f'2022-{month}-{day}',
        'timeZone': 'Europe/Warsaw'
    },
    'end': {
        'date': f'2022-{month}-{day}',
        'timeZone': 'Europe/Warsaw'
    },
    'recurrence': [
    'RRULE:FREQ=YEARLY',
    ]

    }
    return event

  
for person in data:
    name, bd, nd = person
    if bd is not None:
        bdd, bdm = bd
        ev_name = "URODZINY: " + name
        ev = create_event(ev_name, bdd,bdm)
        #_ = service.events().insert(calendarId=cal_id, body=ev).execute()
    if nd is not None:
        bdd, bdm = nd
        ev_name = "IMIENINY: " + name
        ev = create_event(ev_name, bdd,bdm)
        print(ev)
        #_ = service.events().insert(calendarId=cal_id, body=ev).execute()

  

def create_event(name, day, month):
    event = {
    'summary': f'{name}',
    'start': {
        'date': f'2022-{month}-{day}',
        'timeZone': 'Europe/Warsaw'
    },
    'end': {
        'date': f'2022-{month}-{day}',
        'timeZone': 'Europe/Warsaw'
    },
    'recurrence': [
    'RRULE:FREQ=YEARLY',
    ]

    }
    return event

  
created_calendar = service.calendars().insert(body=calendar).execute()
  
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    created_calendar = service.calendars().insert(body=calendar).execute()
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\googleapiclient\_helpers.py", line 130, in positional_wrapper
    return wrapped(*args, **kwargs)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\googleapiclient\http.py", line 923, in execute
    resp, content = _retry_request(
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\googleapiclient\http.py", line 222, in _retry_request
    raise exception
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\googleapiclient\http.py", line 191, in _retry_request
    resp, content = http.request(uri, method, *args, **kwargs)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\google_auth_httplib2.py", line 218, in request
    response, content = self.http.request(
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\httplib2\__init__.py", line 1701, in request
    (response, content) = self._request(
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\httplib2\__init__.py", line 1421, in _request
    (response, content) = self._conn_request(conn, request_uri, method, body, headers)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\site-packages\httplib2\__init__.py", line 1344, in _conn_request
    conn.request(method, request_uri, body, headers)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1276, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1322, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1271, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 1031, in _send_output
    self.send(msg)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\http\client.py", line 992, in send
    self.sock.sendall(data)
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\ssl.py", line 1236, in sendall
    v = self.send(byte_view[count:])
  File "C:\Users\ignsz\AppData\Local\Programs\Python\Python310\lib\ssl.py", line 1205, in send
    return self._sslobj.write(data)
ssl.SSLEOFError: EOF occurred in violation of protocol (_ssl.c:2384)
created_calendar = service.calendars().insert(body=calendar).execute()
  
cal_id = created_calendar["id"]
  
for person in data:
    name, bd, nd = person
    if bd is not None:
        bdd, bdm = bd
        ev_name = "URODZINY: " + name
        ev = create_event(ev_name, bdd,bdm)
        _ = service.events().insert(calendarId=cal_id, body=ev).execute()
    if nd is not None:
        bdd, bdm = nd
        ev_name = "IMIENINY: " + name
        ev = create_event(ev_name, bdd,bdm)
        _ = service.events().insert(calendarId=cal_id, body=ev).execute()
    print(".",end="")

  
............................................................................
