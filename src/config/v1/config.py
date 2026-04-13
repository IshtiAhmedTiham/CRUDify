from pydantic_settings import BaseSettings

class Configuration(BaseSettings):
    @property
    def database_url(self):
        return "sqlite:///app.db"