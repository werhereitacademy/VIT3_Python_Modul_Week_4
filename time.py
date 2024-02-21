# time.py

from datetime import datetime, timedelta
import json
import os

TRACKING_FILE = "tracking.json"

def current_time():
    return datetime.now()

def two_weeks_later():
    return current_time() + timedelta(days=14)

def save_tracking_info(member_info, book_info):
    tracking_data = {
        **member_info,
        **book_info,
        "registration_date": current_time().strftime("%Y-%m-%d %H:%M:%S"),
        "book_return_date": two_weeks_later().strftime("%Y-%m-%d %H:%M:%S")
    }
    if not os.path.exists(TRACKING_FILE):
        with open(TRACKING_FILE, "w") as f:
            json.dump([], f)
    with open(TRACKING_FILE, "r") as f:
        tracking_info = json.load(f)
    tracking_info.append(tracking_data)
    with open(TRACKING_FILE, "w") as f:
        json.dump(tracking_info, f, indent=4)
