"""Weather API client."""

import requests
from settings import settings
import structlog

logger = structlog.get_logger(__name__)


def get_weather(zipcode: int) -> str:
    """Get the weather for a given zipcode."""
    base_url = "http://api.weatherapi.com/v1"

    try:
        response = requests.get(
            f"{base_url}/forecast.json",
            params={"key": settings.WEATHER_API_KEY, "q": zipcode, "days": 3},
        )
        response.raise_for_status()

        data = response.json()
        forecast = data["forecast"]["forecastday"]

        weather_report = []
        for day in forecast:
            date = day["date"]
            condition = day["day"]["condition"]["text"]
            temp = day["day"]["avgtemp_c"]
            weather_report.append(f"{date}: {condition}, {temp}°C")

        return "\n".join(weather_report)

    except requests.RequestException as e:
        logger.error(f"Weather API error: {str(e)}")
        return "Could not fetch weather data"
