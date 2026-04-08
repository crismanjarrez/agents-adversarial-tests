"""
Application configuration loaded from environment variables.
"""
import os


class Config:
    DATABASE_URL: str = os.environ.get("DATABASE_URL", "sqlite:///app.db")
    DEBUG: bool = os.environ.get("DEBUG", "false").lower() == "true"
    SECRET_KEY: str = os.environ.get("SECRET_KEY", "")


def get_config() -> Config:
    return Config()
