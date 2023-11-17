from unittest.mock import MagicMock
from unittest.mock import patch

from app.models.weather import WeatherInfoDB
from app.repositories.weather import WeatherRepository


class TestWeatherRepository:
    @patch.object(WeatherInfoDB, "save")
    def test_insert(self, save_mock: MagicMock):
        weather_repository = WeatherRepository()

        weather_repository.insert(lat=6.9, lon=8.9)

        save_mock.assert_called()
