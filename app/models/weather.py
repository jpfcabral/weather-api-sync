import mongoengine as me
from pydantic import BaseModel


class WeatherInfoResponse(BaseModel):
    """"""


class WeatherInfoModel(BaseModel):
    """"""


class WeatherInfoDB(me.Document):
    """Database Interface"""

    lat = me.DecimalField()
    lon = me.DecimalField()
    request_datetime = me.DateTimeField()
