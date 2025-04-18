from __future__ import annotations

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from llm import llm


WEATHER_PROMPT = """

            You are a weather expert. You will be given a reading of the weather and you need to summarize it for useful info.
            Make sure the information is relevant to the location and date provided.

            This is AMERICA use Fahrenheit and miles per hour for wind speed.

            When you refer to a date, make sure to state the day of week as well.

            {input}

            """

butler_prompt = PromptTemplate(
    template=WEATHER_PROMPT,
    input_variables=["input"],
)

weather_chain = butler_prompt | llm | StrOutputParser()
