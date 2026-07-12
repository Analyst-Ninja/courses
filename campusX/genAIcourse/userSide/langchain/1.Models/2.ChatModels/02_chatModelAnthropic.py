from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv()

model = ChatAnthropic(model="claude-3-7-sonnet-20250219")

result = model.invoke("What is the capital of India?")

print(result.content)
