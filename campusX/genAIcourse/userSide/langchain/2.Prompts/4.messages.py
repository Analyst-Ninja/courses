from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="Hi"),
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)
