from pydantic_settings import BaseSettings

class Configuration(BaseSettings):
    @property
    def Database(self):
        return "postgresql://postgres:hello@localhost/fitness"