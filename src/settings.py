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
    DEFAULT_ZIPCODE: int = 56007
    NEWS_API_KEY: str = ""
    NEWS_TOPICS: list[str] = [
        "artificial intelligence",
        "tariffs",
        "freight",
        "immigration",
    ]
    NEWS_SOURCES: list[str] = [
        "hackernews.com",
        "foxbusiness.com",
        "reuters.com",
        "wsj.com",
    ]
    NEWS_DAYS_BACK: int = 1

    BUTLER_PROMPT: str = "You are Butler, a loyal and steadfast servant to your master. Speak with the honor and discipline of a warrior, much like Captain Garviel Loken of the Luna Wolves. Always address your master with respect and deference, and provide assistance with clarity and precision. Your duty is to serve faithfully, offering guidance and support in all matters, while maintaining the decorum and gravitas befitting a warrior of the Imperium."
    USER_PROFILE: str = "I am a 30 year old male, married with kids. I am a data scientist that loves lifing weights, playing video games, and spending time with my family. I am interested in technology, science, and current events. I enjoy reading about artificial intelligence, machine learning, and data science. I also like to keep up with the latest news in the tech industry. I also enjoy reading about history and the stock market."

    model_config = SettingsConfigDict(
        env_file=(base_path / "config" / "secrets"),
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
