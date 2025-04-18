"""Where the llms are defined and used."""

from __future__ import annotations

from langchain_openai import ChatOpenAI

from settings import settings

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=settings.OPENAI_API_KEY,
)
