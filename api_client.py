import os
import requests
from logger import log_success, log_failure

def poll_apis():
    meraki_key = os.getenv("MERAKI_API_KEY")
    url = "https://api.meraki.com/api/v1/organizations"
    headers = {"X-Cisco-Meraki-API-Key": meraki_key}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        log_success("Meraki API", response.text)
    except Exception as e:
        log_failure("Meraki API", str(e))
