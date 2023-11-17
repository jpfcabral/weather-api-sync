from app.externals.open_weather import OpenWeatherExternal
from app.repositories.weather import WeatherRepository


class WeatherService:
    def __init__(
        self, weather_repository=WeatherRepository(), open_weather_api=OpenWeatherExternal()
    ) -> None:
        """"""
        self.weather_repository = weather_repository
        self.open_weather_api = open_weather_api

    def get_weather_info(self, lat: float, lon: float) -> dict:
        """
        Gets weather information up to 5 days

        Args:
            lat: float = Latitude
            lon: float = Longitude


        Returns
            Reponse with weather information
        """

        weather_info = self.open_weather_api.get_5_day_weather_forecast(lat=lat, lon=lon)
        self.weather_repository.insert(lat=lat, lon=lon)

        return weather_info

    def get_history(self) -> dict:
        """"""
