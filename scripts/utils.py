import numpy as np
from datetime import date, datetime, timedelta

def dcf(date_start, date_end, basis = 'ACT360'):
    if(basis == 'ACT360'):
        return (date_end - date_start).days/360
    else:
        raise ValueError(f"This basis {basis} is not supported.")
