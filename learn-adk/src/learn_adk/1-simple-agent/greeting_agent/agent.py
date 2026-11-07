from google.adk import Agent

root_agent = Agent(
    name="greeting_agent",
    model="gemini-3.5-flash-lite",
    description="Greeting Agent",
    instruction="""
    You are a helpful agent that greets user.
    Ask for the user's name and greet with the user's name.
    """,
)
