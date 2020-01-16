from datetime import date, datetime

Y = 2000  # dummy leap year to allow input X-02-29 (leap day)
seasons = [('1-р улирал', (date(Y, 1, 1), date(Y, 3, 31))),
           ('2-р улирал', (date(Y, 4, 1), date(Y, 6, 30))),
           ('3-р улирал', (date(Y, 7, 1), date(Y, 9, 30))),
           ('4-р улирал', (date(Y, 10, 1), date(Y, 12, 31)))]


def get_season(now):
    if isinstance(now, datetime):
        now = now.date()
    now = now.replace(year=Y)
    return next(season for season, (start, end) in seasons
                if start <= now <= end)
