# from pydantic_settings import BaseSettings, SettingsConfigDict


# class Settings(BaseSettings):
#     database_url: str = "sqlite:///business_sentinel.db"
#     alert_threshold: int = 60
#     log_level: str = "INFO"

#     model_config = SettingsConfigDict(env_prefix="BUSINESS_SENTINEL_", env_file=".env")


# settings = Settings()

import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@localhost:5432/business_sentinel",
)

FLASK_ENV = os.getenv("FLASK_ENV", "development")

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "development-secret-key",
)

RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"
QUARANTINE_DATA_DIR = BASE_DIR / "data" / "quarantine"

RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
QUARANTINE_DATA_DIR.mkdir(parents=True, exist_ok=True)
