from __future__ import annotations

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

from llm import llm
from settings import settings
import datetime
import pytz

BUTLER_DAILY_BUILD_PROMPT = """"
    You are a butler providing a daily morning briefing. Your task is to summarize the following information, {butler_prompt}:

    Use this list of fun facts to make the summary more interesting:
    {fun_facts}

    1. **Weather**: Provide a concise summary of today's weather forecast.
    {weather}
    2. **Tasks**: List the important tasks or appointments for the day.
    {appointments}
    3. **Articles**: Summarize the key points from articles you think I might like based on this user profile:
    **{news_profile}**
    {news}
    4. **ToDos**: Include any notes or reminders that are relevant for the day.
    {todos}
    5. **Miscellaneous**: Any other relevant information or updates.
    {misc}
    The current date is {current_date}. Use this date to ensure all information is relevant and up-to-date.


    Before sending the summary, please ensure that it is well-structured and easy to read. Use bullet points or numbered lists where appropriate.
    It should only take 2-3 minutes to read.

    """


central_tz = pytz.timezone("US/Central")
current_date_central = datetime.datetime.now(central_tz).strftime("%Y-%m-%d")

butler_prompt = PromptTemplate(
    template=BUTLER_DAILY_BUILD_PROMPT,
    input_variables=["fun_facts", "weather", "appointments", "news", "todos", "misc"],
    partial_variables={
        "current_date": current_date_central,
        "butler_prompt": settings.BUTLER_PROMPT,
        "news_profile": settings.USER_PROFILE,
    },
)

daily_chain = butler_prompt | llm | StrOutputParser()
