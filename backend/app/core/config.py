from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[2]

class Settings(BaseSettings):
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_NAME: str ="school_management"
    DB_USER:str = "postgres"
    DB_PASSWORD:str = "B1l1S23a12y"

    model_config = SettingsConfigDict(env_file=BASE_DIR /".env",
                                      env_file_encoding="utf-8",
                                      extra="ignore")

settings = Settings()