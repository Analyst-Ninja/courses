from google.adk.agents import Agent
from google.adk.models import LiteLlm

model = LiteLlm(model="ollama_chat/qwen3.5:0.8b", api_base="http://localhost:11434")

# Create the root agent
question_answering_agent = Agent(
    name="question_answering_agent",
    model=model,
    description="Question answering agent",
    instruction="""
    You are a helpful assistant that answers questions about the user's preferences.

    Here is some information about the user:
    Name: 
    {user_name}
    Preferences: 
    {user_preferences}
    """,
)
