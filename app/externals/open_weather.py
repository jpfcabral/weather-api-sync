import requests

from app.config import settings


class OpenWeatherExternal:
    def __init__(
        self,
        host: str = settings.OPEN_WEATHER_HOST,
        secret_key: str = settings.OPEN_WEATHER_KEY,
    ) -> None:
        """"""

        self.host = host
        self.secret_key = secret_key

    def get_5_day_weather_forecast(
        self,
        lat: float,
        lon: float,
        units: str = "metric",
        mode: str = "standart",
        cnt: int = None,
        lang: str = None,
    ) -> dict:
        """
        Retrieves 5 day forecast for any location on the globe.
        It includes weather forecast data with 3-hour step

        Args:
            lat: float = Latitude.
            lon: float = Longitude.
            units: str = Units of measurement. Example: standard, metric or imperial.
            mode (disabled): str = Response format
            cnt: int = A number of timestamps, which will be returned in the API response
            lang (disabled): str =
        """

        uri: str = f"{self.host}/forecast"

        params: dict[str, any] = {
            "appid": self.secret_key,
            "lat": lat,
            "lon": lon,
            "units": units,
            "mode": mode,
            "cnt": cnt,
            "lang": lang,
        }

        response = requests.post(
            url=uri,
            params=params,
            timeout=10,
        )

        response.raise_for_status()
        content = response.json()

        return content
