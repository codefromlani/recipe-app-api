import os
import requests
import schedule
import time
from datetime import datetime

API_URL = os.getenv("API_URL")

def ping_api():
    if not API_URL:
        print(f"[{datetime.now().isoformat()}] API_URL environment variable not set. Skipping ping.")
        return

    try:
        response = requests.get(API_URL, timeout=5)
        if response.status_code == 200:
            print(f"[{datetime.now().isoformat()}] GET request sent successfully to {API_URL}")
        else:
            print(f"[{datetime.now().isoformat()}] GET request failed with status code {response.status_code} for {API_URL}")
    except requests.exceptions.RequestException as e:
        print(f"[{datetime.now().isoformat()}] Error while sending request to {API_URL}: {e}")
    except Exception as e:
        print(f"[{datetime.now().isoformat()}] An unexpected error occurred: {e}")


schedule.every(14).minutes.do(ping_api)

print(f"[{datetime.now().isoformat()}] Cron job started: Pinging every 14 minutes...")

while True:
    schedule.run_pending()
    time.sleep(1)