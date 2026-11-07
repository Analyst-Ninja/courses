import random

from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm

model = LiteLlm(
    model="ollama_chat/qwen3.5:0.8b",  # "ollama_chat/" + model name from `ollama list`
    api_base="http://localhost:11434",
)


def get_dad_joke():
    jokes = [
        "Why did the chicken cross the road? To get to the other side!",
        "What do you call a belt made of watches? A waist of time.",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
    ]
    return {"joke": random.choice(jokes)}


root_agent = Agent(
    name="dad_joke_agent",
    model=model,
    description="An agent that returns dad jokes",
    instruction="""
    You are a helpful assistant that tell dad jokes 
    which uses the tool below to get yhe `Dad Jokes`
    - get_dad_joke
    """,
    tools=[get_dad_joke],
)
