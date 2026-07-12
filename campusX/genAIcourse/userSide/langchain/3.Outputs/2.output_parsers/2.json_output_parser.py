from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(dotenv_path="../../.env")

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

parser = JsonOutputParser()

# template = PromptTemplate(
#     template="Give the name, age andn city of a fictitious person. \n{format_instruction}",
#     input_variables=[],
#     partial_variables={
#         'format_instruction': parser.get_format_instructions()
#     }
# )

template = PromptTemplate(
    template="Give me 5 facts about the {topic}. \n{format_instruction}",
    input_variables=["topic"],
    partial_variables={"format_instruction": parser.get_format_instructions()},
)

# prompt = template.format()

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# print(final_result, type(final_result))
# print(final_result['name'])

chain = template | model | parser

# result = chain.invoke({}) # have to send the blank dict because we are giving any input
result = chain.invoke({"topic": "black holes"})

print(result)
