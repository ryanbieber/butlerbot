"""Settings File for Nostradamus."""

from __future__ import annotations

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

base_path = Path(__file__).resolve().parent


class Settings(BaseSettings):
    """Base settings for the Nostradamus app."""

    BOT_TOKEN: str = ""
    OPENAI_API_KEY: str = ""
    WEATHER_API_KEY: str = ""

    model_config = SettingsConfigDict(
        env_file=(base_path / "config" / "secrets"),
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
