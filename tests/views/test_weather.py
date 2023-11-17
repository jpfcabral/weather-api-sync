from unittest.mock import MagicMock
from unittest.mock import patch

import pytest
from fastapi import HTTPException
from requests import HTTPError

from app.services.weather import WeatherService
from app.views import weather


class TestWeatherView:
    @patch.object(WeatherService, "get_weather_info")
    def test_get_weather_info(self, get_weather_info_mock: MagicMock):
        weather.get_weather_info(lat=45.6, lon=35.9)

        get_weather_info_mock.assert_called_with(lat=45.6, lon=35.9)

    @patch.object(WeatherService, "get_weather_info")
    def test_get_weather_info_http_error(self, get_weather_info_mock: MagicMock):
        get_weather_info_mock.side_effect = HTTPError()

        with pytest.raises(HTTPException) as _:
            weather.get_weather_info(lat=45.6, lon=35.9)
