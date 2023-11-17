from fastapi import FastAPI

from app.views.weather import router as weather_router

app = FastAPI()

app.include_router(weather_router)
