from dotenv import load_dotenv
from langchain.schema.runnable import RunnableParallel, RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv("../.env")

tweet_prompt = PromptTemplate(
    template="Write a tweet about the topic: {topic}", input_variables=["topic"]
)

linkedin_prompt = PromptTemplate(
    template="Write a LinkedIn post about the topic: {topic}", input_variables=["topic"]
)

tweet_llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.9)

linkedin_llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.5)

parser = StrOutputParser()

# tweet_chain = RunnableSequence(tweet_prompt, tweet_llm, parser)
# linkedin_chain = RunnableSequence(linkedin_prompt, linkedin_llm, parser)

# parallel_chain = RunnableParallel(
#     {
#     "tweet":tweet_chain,
#     "linkedIn":linkedin_chain
#     }
# )

# Alternative Way

parallel_chain = RunnableParallel(
    {
        "tweet": RunnableSequence(tweet_prompt, tweet_llm, parser),
        "linkedIn": RunnableSequence(linkedin_prompt, linkedin_llm, parser),
    }
)

print(parallel_chain.invoke({"topic": "AI"}))
