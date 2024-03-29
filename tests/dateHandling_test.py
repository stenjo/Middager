from datetime import datetime, timezone
from dateHandling import dayText, isNowInTimePeriod

def test_isNowInTimePeriod():
    startTime = datetime.strptime("2023-10-22T10:12", "%Y-%m-%dT%H:%M")
    endTime = datetime.strptime("2023-10-25T10:12", "%Y-%m-%dT%H:%M")
    today = datetime.strptime("2023-10-23T10:12", "%Y-%m-%dT%H:%M")
    before = datetime.strptime("2023-10-22T10:11", "%Y-%m-%dT%H:%M")
    after = datetime.strptime("2023-10-25T10:13", "%Y-%m-%dT%H:%M")
    
    assert isNowInTimePeriod(startTime, endTime, today) == True
    assert isNowInTimePeriod(startTime, endTime, before) == False
    assert isNowInTimePeriod(startTime, endTime, after) == False


today = datetime.strptime("2023-10-23T10:12", "%Y-%m-%dT%H:%M").replace(tzinfo=timezone.utc)
    
def test_dayText_tomorrow():
    event = {
        'start': {
            'date': '2023-10-24'
        },
        'summary': 'Event summary'
    }
    
    assert dayText(event, today) == "I morgen: Event summary"

def test_dayText_today():
    event = {
        'start': {
            'date': '2023-10-23'
        },
        'summary': 'Event summary'
    }
    
    assert dayText(event, today) == "I dag: Event summary"
    
def test_dayText_today_with_time():
    event = {
        'start': {
            'date': '2023-10-23',
            'dateTime': '2023-10-23T10:22:18'
        },
        'summary': 'Event summary'
    }
    
    assert dayText(event, today) == "I dag: Event summary kl. 10:22"
    
def test_dayText_friday():
    event = {
        'start': {
            'date': '2023-10-27'
        },
        'summary': 'Event summary'
    }
    
    assert dayText(event, today) == "Fredag: Event summary"
    
def test_dayText_friday_plus_one_week():
    event = {
        'start': {
            'date': '2023-11-03'
        },
        'summary': 'Event summary'
    }
    
    assert dayText(event, today) == "Fredag 03/11: Event summary"

def test_dayText_today_with_time_and_timezone():
    event = {
        'start': {
            'date': '2023-10-23',
            'dateTime': '2023-10-23T10:22:18+01:00'
        },
        'summary': 'Event summary'
    }
    today = datetime.strptime("2023-10-23T10:12 +0100", "%Y-%m-%dT%H:%M %z")
    # print(today)
    # dt:  2023-11-09 13:15:00+01:00
    # today:  2023-11-04 18:54:37.512734

    assert dayText(event, today) == "I dag: Event summary kl. 10:22"
    
def test_dayText_today_with_datetime_and_timezone():
    event = {
        'start': {
            'date': datetime.today().strftime('%Y-%m-%d'),
            'dateTime': datetime.today().strftime('%Y-%m-%d') + 'T10:22:18+01:00'
        },
        'summary': 'Event summary'
    }

    assert dayText(event) == "I dag: Event summary kl. 10:22"

def test_dayText_today_with_date_and_no_timezone():
    event = {
        'start': {
            'date': datetime.today().strftime('%Y-%m-%d'),
        },
        'summary': 'Event summary'
    }

    assert dayText(event) == "I dag: Event summary"

