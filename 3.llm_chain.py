from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI

load_dotenv()

# Initialized the LLM
llm = GoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7)

# Creating the prompt
prompt = PromptTemplate(
    template="Suggest a catchy blog title for the topic:- {topic}",
    input_variables=["topic"],
)

# Create a LLMChain
chain = LLMChain(llm=llm, prompt=prompt)

# Run the chain with specific topic
topic = input("Enter the topic: ")
output = chain.run(topic)

print("Generated blog title: ", output)
