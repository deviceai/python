from datetime import datetime, date

def get_age(birth_date, current_date=None):
    if current_date is None:
        now = date.today()
    else:
        now = current_date
    return now.year - birth_date.year - ((now.month, now.day) < (birth_date.month, birth_date.day))

