from typing import List
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    # API配置
    API_V1_PREFIX: str = "/api/v1"
    DEBUG: bool = True
    PROJECT_NAME: str = "Focus AI API"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "Focus AI Backend API"

    # 数据库配置
    DATABASE_URL: str
    SQL_ECHO: bool = False  # 是否打印SQL语句

    # JWT配置
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # CORS配置
    ALLOWED_ORIGINS: str

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings() -> Settings:
    return Settings()
