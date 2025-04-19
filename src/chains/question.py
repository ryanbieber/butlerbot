from __future__ import annotations

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

from llm import llm
from settings import settings
import datetime
import pytz

EXPERT_ANSWER = """
            You are an expert in your field. Provide a detailed and accurate answer to the user's question. Ensure your response is well-researched, factual, and free from errors. Avoid making assumptions or providing generic AI-generated content. If you are unsure, clearly state that and suggest further steps for clarification or research.

            Make sure to also include any relevant sources or references that support your answer. Your response should be comprehensive and cover all aspects of the question.

            It shouldn't be more than 2-3 paragraphs long, Unless the question is very complex, in which case you can provide a more detailed response.

            {butler_prompt}

            Question: {input}
            """


central_tz = pytz.timezone("US/Central")
current_date_central = datetime.datetime.now(central_tz).strftime("%Y-%m-%d")

butler_prompt = PromptTemplate(
    template=EXPERT_ANSWER,
    input_variables=["input"],
    partial_variables={
        "current_date": current_date_central,
        "butler_prompt": settings.BUTLER_PROMPT,
    },
)

question_chain = butler_prompt | llm | StrOutputParser()
