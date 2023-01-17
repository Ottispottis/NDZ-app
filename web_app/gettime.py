import datetime

from datetime import datetime, timezone


# Getting current time that is used to determine if 10 minutes have passed from the time a pilot violated the NDZ
def current_time():
    now = datetime.now(timezone.utc)
    now_time = now.strftime('%d/%m/%Y %H:%M:%S')
    return now_time
