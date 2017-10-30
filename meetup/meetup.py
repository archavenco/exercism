from calendar import day_name, isleap
from datetime import date, timedelta


STARTS = {
    '1st': 1,
    '2nd': 8,
    '3rd': 15,
    '4th': 22,
    '5th': 29,
    'teenth': 13,
}


def meetup_day(year, month, day, case):
    start = date(year, month, STARTS.get(case, last_day_start(year, month)))
    offset = list(day_name).index(day) - start.weekday()
    return start + timedelta(days=offset % 7)


def last_day_start(year, month):
    return([25, 22 + int(isleap(year))] + [25, 24, 25, 24, 25] * 2)[month - 1]