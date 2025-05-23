from __future__ import annotations

from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate

from llm import llm
from models import Note
from settings import settings
import datetime
import pytz

BUTLER_NOTE_PROMPT = """
            You will be given a note and you need to categorize and summarize it for useful info.
            Make sure to store relevant information in the correct fields.

            {butler_prompt}

            The current date is {current_date}, use that date if people reference tomorrow or next monday, etc.

            {input}

            {format_instructions}

            """


parser = PydanticOutputParser(pydantic_object=Note)

central_tz = pytz.timezone("US/Central")
current_date_central = datetime.datetime.now(central_tz).strftime("%Y-%m-%d")

butler_prompt = PromptTemplate(
    template=BUTLER_NOTE_PROMPT,
    input_variables=["input"],
    partial_variables={
        "format_instructions": parser.get_format_instructions(),
        "current_date": current_date_central,
        "butler_prompt": settings.BUTLER_PROMPT,
    },
)

category_chain = butler_prompt | llm | parser
