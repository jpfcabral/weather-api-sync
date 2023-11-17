from unittest.mock import MagicMock
from unittest.mock import patch

from app.externals.open_weather import OpenWeatherExternal


class TestOpenWeatherExternal:
    def setup_method(self):
        self.host = "mocked-host"
        self.secret_key = "mocked-secret-key"
        self.instance = OpenWeatherExternal(host=self.host, secret_key=self.secret_key)

    @patch("requests.post")
    def test_get_5_day_weather_forecast(self, post_mock: MagicMock):

        self.instance.get_5_day_weather_forecast(lat=45.6, lon=89.6)

        post_mock.assert_called_once_with(
            url=f"{self.host}/forecast",
            timeout=10,
            params={
                "appid": self.secret_key,
                "lat": 45.6,
                "lon": 89.6,
                "units": "metric",
                "mode": "standart",
                "cnt": None,
                "lang": None,
            },
        )
