from pydantic_settings import BaseSettings

class Configuration(BaseSettings):
    @property
    def sqlite_database(self):
        return "sqlite:///app.db"
    
    @property
    def postgresql_database(self):
        return "sqlite:///app.db"