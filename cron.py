from apscheduler.schedulers.blocking import BlockingScheduler
import requests
from datetime import datetime
import os

API_URL = os.getenv("API_URL")

def ping_api():
    try:
        res = requests.get(API_URL)
        if res.status_code == 200:
            print(f"[{datetime.now()}] Success")
        else:
            print(f"[{datetime.now()}] Failed: {res.status_code}")
    except Exception as e:
        print(f"[{datetime.now()}] Error: {e}")

scheduler = BlockingScheduler()
scheduler.add_job(ping_api, 'cron', minute='*/14')

print("Cron job running every 14 minutes...")
scheduler.start()
