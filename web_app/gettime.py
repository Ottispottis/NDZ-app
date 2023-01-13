import datetime

from datetime import datetime, timezone


# Getting current time
def current_time():
    now = datetime.now(timezone.utc)
    now_time = now.strftime('%d/%m/%Y %H:%M:%S')
    return now_time
