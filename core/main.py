import datetime


def year_choices():
    choice = [(r,r) for r in range(1991, datetime.date.today().year+1)]
    return tuple(choice)

print(year_choices())
