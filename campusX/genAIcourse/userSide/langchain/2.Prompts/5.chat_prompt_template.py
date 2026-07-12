from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate(
    [
        ("system", "you are a {domain} expert"),
        ("human", "explain in simple terms, what is {topic}"),
    ]
)

prompt = chat_template.invoke({"domain": "doctor", "topic": "amoeba"})

print(prompt)
