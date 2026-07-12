from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(dotenv_path="../.env")

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

prompt1 = PromptTemplate(
    template="Genrate detailed report on {topic}", input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate the 5 lines summary of: {text}", input_variables=["text"]
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

res = chain.invoke({"topic": "cricket"})

print(res)
# chain.get_graph().print_ascii()
