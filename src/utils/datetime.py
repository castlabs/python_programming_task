from datetime import datetime
from time import time


def format_datetime_date(datetime_value: datetime) -> str:
    DATE_NOTATION = "%Y-%m-%d"
    return datetime_value.strftime(DATE_NOTATION)


def generate_now() -> datetime:
    return datetime.now()


def generate_seconds_since_epoch() -> int:
    return int(time())
