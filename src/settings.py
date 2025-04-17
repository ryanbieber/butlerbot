"""Settings File for Nostradamus."""
from __future__ import annotations

import os

from pydantic_settings import BaseSettings
from pathlib import Path


base_path = Path(__file__).resolve().parent

class Settings(BaseSettings):
    """Base settings for the Nostradamus app."""
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")

    class Config:
        env_file = base_path / "config" / "secrets"



settings = Settings()