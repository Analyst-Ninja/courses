from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv("../.env")

path = "https://www.amazon.in/Apple-MacBook-13-inch-8%E2%80%91core-Unified/dp/B0DLHYCZMV/ref=asc_df_B0DLHYCZMV/?tag=googleshopdes-21&linkCode=df0&hvadid=709855510254&hvpos=&hvnetw=g&hvrand=1604183894405937361&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9210829&hvtargid=pla-2375129355066&psc=1&mcid=b09dfdf4fa5b33c8b7f5639a1ec4bc36&tag=googleshopdes-21&linkCode=df0&hvadid=709855510254&hvpos=&hvnetw=g&hvrand=1604183894405937361&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9210829&hvtargid=pla-2375129355066&psc=1&gad_source=1"
loader = WebBaseLoader(web_path=path)

docs = loader.load()

# print(len(docs))

# print(docs[0].page_content)

prompt = PromptTemplate(
    template="Answer the following question \n{question} based on the following text:\n{text}",
    input_variables=["question", "text"],
)

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

parser = StrOutputParser()

chain = prompt | model | parser

res = chain.invoke(
    {
        # 'question': 'What is the product we are talking about?',
        # 'question': 'What is the price?',
        "question": "What is the screen size?",
        "text": docs[0].page_content,
    }
)

print(res)
