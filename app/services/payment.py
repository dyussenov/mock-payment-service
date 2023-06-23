import requests

from app.settings import settings


def send_confirmation(user_id: int, event_id: int):
    json_data = {
        "user_id": user_id,
        "event_id": event_id,
    }
    response = requests.post(settings.confirmation_url, json=json_data)
    return response
