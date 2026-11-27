from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[2]

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int


    model_config = SettingsConfigDict(env_file=BASE_DIR /".env",
                                      env_file_encoding="utf-8",
                                      case_sensitive=True,
                                      extra="ignore")

settings = Settings()