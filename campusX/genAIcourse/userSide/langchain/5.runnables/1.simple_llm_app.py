from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI

load_dotenv(".env")

# Initializing the LLM
model = GoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.5)

# Creating the prompt
prompt = PromptTemplate(
    template="Suggest a catchy blog title for the topic:- {topic}",
    input_variables=["topic"],
)

# Taking the topic from the user
topic = input("Enter the topic: ")

# Finalizing the prompt with user topic
final_prompt = prompt.format(topic=topic)

# Calling the LLM directlt
blog_title = model.predict(final_prompt)

print(blog_title)
