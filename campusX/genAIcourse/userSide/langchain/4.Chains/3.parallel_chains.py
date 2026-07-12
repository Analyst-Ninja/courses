from dotenv import load_dotenv
from langchain.schema.runnable import RunnableParallel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(dotenv_path="../.env")

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

prompt1 = PromptTemplate(
    template="Generate short and simple note from the following text: \n{text}",
    input_variables=["text "],
)

prompt2 = PromptTemplate(
    template="Generate 5 short quiz question from the following text: \n{text}",
    input_variables=["text"],
)

prompt3 = PromptTemplate(
    template="Merge the provided notes and quiz question in a single documents:\nnotes: \n{notes} \nquiz qusetion:\n{quiz}",
    input_variables=["notes", "quiz"],
)

parser = StrOutputParser()

# Parallel Chain Creation
parallel_chain = RunnableParallel(
    {"notes": prompt1 | model | parser, "quiz": prompt2 | model | parser}
)

merge_chain = prompt3 | model | parser

chain = parallel_chain | merge_chain

res = chain.invoke({"text": input("Text:\n")})

print(res)

chain.get_graph().print_ascii()
