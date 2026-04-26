import requests
from datetime import datetime

def calculate_account_age(created_at):
    created_date = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ")
    today = datetime.utcnow()

    age_years = today.year - created_date.year

    # adjust if birthday hasn't occurred yet this year
    if (today.month, today.day) < (created_date.month, created_date.day):
        age_years -= 1

    return age_years