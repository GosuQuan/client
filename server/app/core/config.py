from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Focus AI"
    
    # Database settings
    DATABASE_URL: str = "mysql+pymysql://root@localhost/focus_ai"
    
    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()
