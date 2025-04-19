from newsapi import NewsApiClient
from typing import List, Dict
from datetime import datetime, timedelta
from settings import settings


class NewsFetcher:
    def __init__(self, api_key: str):
        """Initialize NewsAPI client with your API key."""
        self.api = NewsApiClient(api_key=api_key)

    def get_personalized_news(
        self,
        topics: List[str],
        preferred_sources: List[str] = None,
        days_back: int = 7,
        language: str = "en",
    ) -> List[Dict]:
        """
        Fetch news based on personal preferences.

        Args:
            topics: List of topics/keywords to search for
            preferred_sources: List of preferred news sources (domains)
            days_back: How many days back to search
            language: Language of news articles

        Returns:
            List of news articles matching criteria
        """
        # Calculate date range
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days_back)

        all_articles = []

        # Search for each topic
        for topic in topics:
            query = topic

            # Add source filtering if specified
            if preferred_sources:
                domains = ",".join(preferred_sources)
                query = f"{query} AND domains:{domains}"

            try:
                response = self.api.get_everything(
                    q=query,
                    from_param=start_date.strftime("%Y-%m-%d"),
                    to=end_date.strftime("%Y-%m-%d"),
                    language=language,
                    sort_by="relevancy",
                )

                if response["status"] == "ok":
                    all_articles.extend(response["articles"])

            except Exception as e:
                print(f"Error fetching news for topic '{topic}': {str(e)}")

        # Remove duplicates based on article URL
        unique_articles = {article["url"]: article for article in all_articles}
        return list(unique_articles.values())

    def get_top_headlines(
        self,
        country: str = None,
        category: str = None,
        sources: List[str] = None,
        language: str = "en",
    ) -> List[Dict]:
        """
        Fetch top headlines for a specific country, category, or sources.

        Args:
            country: Country code (e.g., 'us', 'gb') for headlines
            category: News category (e.g., 'business', 'sports')
            sources: List of specific news sources
            language: Language of news articles

        Returns:
            List of top headlines
        """
        try:
            response = self.api.get_top_headlines(
                country=country,
                category=category,
                sources=",".join(sources) if sources else None,
                language=language,
            )

            if response["status"] == "ok":
                return response["articles"]
            else:
                print(
                    f"Error fetching top headlines: {response.get('message', 'Unknown error')}"
                )
                return []

        except Exception as e:
            print(f"Error fetching top headlines: {str(e)}")
            return []


def get_top_us_news_by_category():
    """Fetch top news headlines from the US for specific categories."""

    # Initialize the news fetcher
    news_fetcher = NewsFetcher(settings.NEWS_API_KEY)

    categories = [
        "business",
        "entertainment",
        "general",
        "health",
        "science",
        "sports",
        "technology",
    ]
    news_by_category = {}

    for category in categories:
        news_by_category[category] = news_fetcher.get_top_headlines(
            country="us",
            category=category,
        )

    return news_by_category
