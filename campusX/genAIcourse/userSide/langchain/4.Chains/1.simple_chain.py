from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(dotenv_path="../.env")

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

template = PromptTemplate(
    template="write 5 lines about {topic}", input_variables=["topic"]
)

parser = StrOutputParser()

chain = template | model | parser

res = chain.invoke({"topic": "tsunami"})

print(res)

chain.get_graph().print_ascii()
