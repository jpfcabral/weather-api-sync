from datetime import datetime

from app.models.weather import WeatherInfoDB


class WeatherRepository:
    def __init__(self) -> None:
        pass

    def read_all_request_info(self):
        """"""

    def insert(self, lat: float, lon: float) -> dict:
        """Insert weather request info into database"""

        weather_db = WeatherInfoDB(lat=lat, lon=lon, request_datetime=datetime.now())
        weather_db.save()

        return weather_db.to_mongo().to_dict()
