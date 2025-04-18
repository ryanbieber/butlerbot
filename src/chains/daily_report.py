from __future__ import annotations

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

from llm import llm

import datetime
import pytz


BUTLER_DAILY_BUILD_PROMPT = """"
    You are a butler providing a daily morning briefing. Your task is to summarize the following information, make
    sure to do it in a formal tone. I want to feel like I am in the Victorian era. When referring to me, use Sir:

    Use this list of fun facts to make the summary more interesting:
    {fun_facts}

    1. **Weather**: Provide a concise summary of today's weather forecast.
    {weather}
    2. **Tasks**: List the important tasks or appointments for the day.
    {appointments}
    3. **Articles**: Summarize the key points from your favorite articles, grouped by their source.
    {news}
    4. **Notes**: Include any notes or reminders that are relevant for the day.
    {notes}
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
    input_variables=["fun_facts", "weather", "appointments", "news", "notes", "misc"],
    partial_variables={"current_date": current_date_central},
)

daily_prompt = butler_prompt | llm | StrOutputParser()
