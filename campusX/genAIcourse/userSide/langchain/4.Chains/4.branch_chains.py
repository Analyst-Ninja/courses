from typing import Literal

from dotenv import load_dotenv
from langchain.schema.runnable import RunnableBranch, RunnableLambda, RunnableParallel
from langchain_core.output_parsers import PydanticOutputParser, StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field

load_dotenv(dotenv_path="../.env")

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

parser = StrOutputParser()


class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description="Give the sentiment of the feedback"
    )


pydantic_parser = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="Classify the sentiment of feedback text into postive and negative.\n{feedback}\n{format_instructions}",
    input_variables=["feedback"],
    partial_variables={
        "format_instructions": pydantic_parser.get_format_instructions()
    },
)

classifier_chain = prompt1 | model | pydantic_parser

prompt2 = PromptTemplate(
    template="Write an appropriate response to this postive feedback:\n{feedback}",
    input_variables=["feedback"],
)

prompt3 = PromptTemplate(
    template="Write an appropriate response to this negative feedback:\n{feedback}",
    input_variables=["feedback"],
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", prompt2 | model | parser),
    (lambda x: x.sentiment == "negative", prompt3 | model | parser),
    RunnableLambda(lambda x: "Could not find the sentiment"),
)

final_chain = classifier_chain | branch_chain

print(final_chain.invoke({"feedback": "product is very good"}))

final_chain.get_graph().print_ascii()
