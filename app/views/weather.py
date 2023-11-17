from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Response
from loguru import logger
from requests import HTTPError

from app.services.weather import WeatherService

router = APIRouter(prefix="/weather", tags=["Weather"])


@router.get(path="/")
def get_weather_info(lat: float = 44.35, lon: float = 10.99) -> Response:
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

        return service.get_weather_info(lat=lat, lon=lon)
    except HTTPError as exc:
        logger.warning(f"Failure to get weather info: {exc}")
        detail = {
            "message": "Error trying to access 3rd party API's",
        }
        raise HTTPException(status_code=503, detail=detail)


@router.get(path="/history")
def get_requests_history(items_per_page: int = 5, page_nb: int = 1) -> Response:
    """
    Gets search history

    Args:
        items_per_page: int = Number of documents por request
        page_nb: int = Page to request
    """
    try:
        service = WeatherService()

        return service.get_history(items_per_page=items_per_page, page_nb=page_nb)
    except Exception as exc:
        logger.error(f"Error retrieving history: {str(exc)}")
        raise
