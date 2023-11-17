from datetime import datetime
from typing import Optional

import mongoengine as me
from pydantic import BaseModel


class WeatherInfoResponse(BaseModel):
    """"""


class WeatherInfoModel(BaseModel):
    """"""


class WeatherData(me.EmbeddedDocument):
    city_id = me.IntField()
    temp = me.DecimalField()
    humidity = me.DecimalField()
