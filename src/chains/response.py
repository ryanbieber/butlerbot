from __future__ import annotations

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

from llm import llm
from settings import settings
import datetime
import pytz

BUTLER_NOTE_PROMPT = """
            You have just received a note. You just need to summarize it and respond that you have taken the note.

            {butler_prompt}

            The current date is {current_date}, use that date if people reference tomorrow or next monday, etc.

            {input}

            """


central_tz = pytz.timezone("US/Central")
current_date_central = datetime.datetime.now(central_tz).strftime("%Y-%m-%d")

butler_prompt = PromptTemplate(
    template=BUTLER_NOTE_PROMPT,
    input_variables=["input"],
    partial_variables={
        "current_date": current_date_central,
        "butler_prompt": settings.BUTLER_PROMPT,
    },
)

response_chain = butler_prompt | llm | StrOutputParser()
