import mongoengine as me
from fastapi import FastAPI

from app.config import settings
from app.views.weather import router as weather_router

app = FastAPI()
app.include_router(weather_router)

me.connect(host=settings.DB_HOST, db=settings.DB_NAME)


@app.get("/")
def status_check():
    return {"status": "ok"}
