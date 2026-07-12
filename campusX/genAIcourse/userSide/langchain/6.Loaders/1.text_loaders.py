from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

loader = TextLoader(file_path="hp4.txt", encoding="utf-8")

# It loads the data in list of documents
docs = loader.load()

# print(type(docs), len(docs), type(docs[0]))

# print(docs[0].page_content)

# print(docs[0].metadata)

prompt = PromptTemplate(
    template="Write a summary for the following text:\n{text}", input_variables=["text"]
)

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

parser = StrOutputParser()

chain = prompt | model | parser

res = chain.invoke({"text": docs[0].page_content})

print(res)
