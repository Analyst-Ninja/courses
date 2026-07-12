from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Chat template
chat_template = ChatPromptTemplate(
    [
        ("system", "you are a helpful customer service agent"),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{query}"),
    ]
)

chat_history = []
# Load chat history
with open("chat_history.txt", "r") as f:
    chat_history.extend(f.readlines())

print(chat_history)

# Create prompt
prompt = chat_template.invoke(
    {"chat_history": chat_history, "query": "Where is my refund"}
)


result = model.invoke(prompt)

print(result.content)
