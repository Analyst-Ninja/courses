from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import (
    ChatHuggingFace,
    HuggingFaceEndpoint,
    HuggingFacePipeline,
)

load_dotenv(dotenv_path="../../.env")

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0", task="text-generation"
)

model = ChatHuggingFace(llm=llm)

# 1st Prompt -> Detailed Report
template1 = PromptTemplate(
    template="Write a detailed report on {topic} consisting of only 10 lines",
    input_variables=["topic"],
)

# 2nd Prompt -> Summary
template2 = PromptTemplate(
    template="Write a 5 lines summary on the following: \n {text}",
    input_variables=["text"],
)

# # Without the StrOutputParser and Chain
# prompt1 = template1.invoke({
#     'topic': 'black hole'
# })

# result = model.invoke(prompt1)

# prompt2 = template2.invoke({
#     'text': result.content
# })

# result2  = model.invoke(prompt2)

# print(result2)

# Instantiating a StrOutputParser object
paser = StrOutputParser()

chain = template1 | model | paser | template2 | model | paser

result = chain.invoke({"topic": "black hole"})

print(result)
