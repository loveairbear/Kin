from datetime import datetime, timedelta
import pytz

# do edge case of daylight savings transition
# which raise error type  pytz.exceptions.AmbiguousTimeError


def utc_to_tz(gmtoffset):
    """
    convert utc offset to a timezone in Olson format for use in pytz

    gmtoffset  - gmtoffset can be an unsigned integer or float
    """
    offset = timedelta(hours=gmtoffset)
    now = datetime.now()
    if(gmtoffset > 14 or gmtoffset < -12):
        raise 'incorrect utc offset'
    for tz in map(pytz.timezone, pytz.common_timezones_set):
        if tz.utcoffset(now) == offset:
            return str(tz)


def find_day(date, day):
    ''' given a datetime object it will return a modified datetime
        with the day of the month set to the next time the specified
        day occurs
        :params date: datetime object, could be timezone aware
                day : integer from 0 to 6 (0 is Monday, 6 is Sunday)
    '''
    assert day < 7
    assert day >= 0
    tmp = date
    day_diff = (day - tmp.weekday()) % 7
    tmp = tmp + timedelta(days=day_diff)
    
    return tmp