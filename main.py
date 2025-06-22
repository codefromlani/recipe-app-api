from fastapi import FastAPI
from datetime import datetime

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