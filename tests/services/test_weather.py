from unittest.mock import MagicMock

from app.services.weather import WeatherService


class TestWeatherService:
    def test_get_weather_info(self):
        weather_repository_mock = MagicMock()
        open_weather_api_mock = MagicMock()

        weather_service = WeatherService(
            weather_repository=weather_repository_mock,
            open_weather_api=open_weather_api_mock,
        )

        weather_service.get_weather_info(lat=65.9, lon=89.9)

        open_weather_api_mock.get_5_day_weather_forecast.assert_called_with(lat=65.9, lon=89.9)
        weather_repository_mock.insert.assert_called_with(lat=65.9, lon=89.9)

    def test_get_history(self):
        weather_repository_mock = MagicMock()
        open_weather_api_mock = MagicMock()

        weather_service = WeatherService(
            weather_repository=weather_repository_mock,
            open_weather_api=open_weather_api_mock,
        )

        weather_service.get_history(page_nb=2, items_per_page=10)

        weather_repository_mock.read_all_request_info.assert_called_with(
            page_nb=2, items_per_page=10
        )
