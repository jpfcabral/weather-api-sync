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

    @patch.object(WeatherInfoDB, "objects")
    def test_read_all_request_info(self, objects_mock: MagicMock):
        skiped_query = MagicMock()
        skiped_query.limit.return_value = [MagicMock(), MagicMock()]
        objects_mock.skip.return_value = skiped_query
        weather_repository = WeatherRepository()

        weather_repository.read_all_request_info(items_per_page=10, page_nb=5)

        objects_mock.skip.assert_called_with(40)
        skiped_query.limit.assert_called_with(10)
