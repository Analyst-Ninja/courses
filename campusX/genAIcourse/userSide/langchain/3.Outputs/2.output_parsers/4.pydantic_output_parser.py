from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field

load_dotenv(dotenv_path="../../.env")

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")


# Schema creation using Pydantic
class Person(BaseModel):

    name: str = Field(description="name of the person")
    age: int = Field(le=100, ge=0, description="age of the person")
    city: str = Field(description="city of a person belongs to")


parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Generate the name, age & city of a ficticious {place} person \n{format_instructions}",
    input_variables=["place"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = template | model | parser

result = chain.invoke({"place": "Nepal"})

print(result, type(result))
