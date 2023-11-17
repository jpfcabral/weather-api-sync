import mongoengine as me


class WeatherInfoDB(me.Document):
    """Database Interface"""

    lat = me.DecimalField()
    lon = me.DecimalField()
    request_datetime = me.DateTimeField()
