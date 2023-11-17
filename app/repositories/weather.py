from datetime import datetime

from app.models.weather import WeatherInfoDB


class WeatherRepository:
    def __init__(self) -> None:
        pass

    def read_all_request_info(self, items_per_page: int, page_nb: int):
        """
        Read/Paginate requests history

        Args:
            items_per_page: int = Number of documents por request
            offset: int = Page to request
        """

        offset = (page_nb - 1) * items_per_page

        objects = list(WeatherInfoDB.objects.skip(offset).limit(items_per_page))
        result = [obj.to_mongo().to_dict() for obj in objects]

        for r in result:
            del r["_id"]

        return result

    def insert(self, lat: float, lon: float) -> dict:
        """
        Insert weather request info into database

        Args:
            lat: float = Latitude
            lon: float = Longitude
        """

        weather_db = WeatherInfoDB(lat=lat, lon=lon, request_datetime=datetime.now())
        weather_db.save()

        return weather_db.to_mongo().to_dict()
