from django.core.exceptions import ValidationError
from datetime import datetime


def validate_date(value):
    try:
        datetime.strptime(str(value), "%Y-%m-%d")

        return True
    except ValueError:
        raise ValidationError("Invalid date format, should be YYYY-MM-DD")


def validate_title(value):
    if not len(str(value).split()) > 1:
        raise ValidationError("Title should be more than one word")
