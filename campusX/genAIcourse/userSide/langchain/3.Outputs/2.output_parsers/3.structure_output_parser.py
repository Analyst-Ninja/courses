from dotenv import load_dotenv
from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv(dotenv_path="../../.env")

# Define a model
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

schema = [
    ResponseSchema(name="fact_1", description="fact 1 about the topic"),
    ResponseSchema(name="fact_2", description="fact 1 about the topic"),
    ResponseSchema(name="fact_3", description="fact 1 about the topic"),
]

parser = StructuredOutputParser(response_schemas=schema)

template = PromptTemplate(
    template="Give 3 facts about the topic: {topic} \n{format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# prompt = template.invoke({
#     'topic' : 'black holes'
# })

# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

# print(final_result)

# With Chain
chain = template | model | parser

final_result = chain.invoke({"topic": "black holes"})

print(final_result)
