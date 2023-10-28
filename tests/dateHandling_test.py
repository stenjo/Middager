import datetime

from dateHandling import dayText, isNowInTimePeriod

def test_isNowInTimePeriod():
    startTime = datetime.datetime.strptime("2023-10-22T10:12", "%Y-%m-%dT%H:%M")
    endTime = datetime.datetime.strptime("2023-10-25T10:12", "%Y-%m-%dT%H:%M")
    today = datetime.datetime.strptime("2023-10-23T10:12", "%Y-%m-%dT%H:%M")
    before = datetime.datetime.strptime("2023-10-22T10:11", "%Y-%m-%dT%H:%M")
    after = datetime.datetime.strptime("2023-10-25T10:13", "%Y-%m-%dT%H:%M")
    
    assert isNowInTimePeriod(startTime, endTime, today) == True
    assert isNowInTimePeriod(startTime, endTime, before) == False
    assert isNowInTimePeriod(startTime, endTime, after) == False


today = datetime.datetime.strptime("2023-10-23T10:12", "%Y-%m-%dT%H:%M")
    
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

