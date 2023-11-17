from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Response
from loguru import logger
from requests import HTTPError

from app.services.weather import WeatherService

router = APIRouter(prefix="/weather")


@router.get(path="/")
async def get_weather_info(lat: float = 44.35, lon: float = 10.99) -> Response:
    """
    Gets weather information up to 5 days

    Args:
        lat: float = Latitude
        lon: float = Longitude


    Returns
        Reponse with weather information
    """
    try:
        service = WeatherService()

        return await service.get_weather_info(lat=lat, lon=lon)
    except HTTPError as exc:
        logger.warning(f"Failure to get weather info: {exc}")
        detail = {
            "message": "Error trying to access 3rd party API's",
        }
        raise HTTPException(status_code=503, detail=detail)


@router.get(path="/history")
def get_requests_history() -> Response:
    """"""
