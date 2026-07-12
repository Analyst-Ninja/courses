from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(
    model="gpt-4", temperature=0.5, max_completion_tokens=100
)  # no of required token in o/p)

result = model.invoke("What is the capital of India?")

print(result.content)
