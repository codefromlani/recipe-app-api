from fastapi import FastAPI
from datetime import datetime
import schedule
import time
import requests
import os

from db.database import engine, Base
from api.favorite import router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Recipe-app API",
)

app.include_router(router, prefix="/api")


@app.get("/")
async def read_root():
    return {"Hello": "Welcome to Recipe-app API"}

@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "message": "Application is healthy.",
        "timestamp": datetime.now().isoformat()
    }


API_URL = os.getenv("API_URL") 

def ping_api():
    try:
        response = requests.get(API_URL, timeout=5)
        if response.status_code == 200:
            print(f"[{datetime.now().isoformat()}] GET request sent successfully")
        else:
            print(f"[{datetime.now().isoformat()}] GET request failed with status code", response.status_code)
    except Exception as e:
        print(f"[{datetime.now().isoformat()}] Error while sending request:", e)

schedule.every(14).minutes.do(ping_api)

print("Cron job started: Pinging every 14 minutes...")

while True:
    schedule.run_pending()
    time.sleep(1)
