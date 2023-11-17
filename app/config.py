from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    API_PORT: int = 8000

    OPEN_WEATHER_KEY: str = ""
    OPEN_WEATHER_HOST: str = ""

    DB_HOST: str = "mongodb://localhost:27017/"
    DB_NAME: str = "test-db"


settings = Settings()
