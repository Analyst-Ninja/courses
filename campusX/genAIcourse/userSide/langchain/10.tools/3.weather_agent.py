from langchain_core.tools import tool
import requests
import os
from dotenv import load_dotenv
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from langchain_ollama.llms import OllamaLLM


load_dotenv()

search_tool = DuckDuckGoSearchRun()


@tool
def get_weather_data(city: str) -> str:
    """
    This function fetches the current weather data for a given city.
    """
    url = f"http://api.weatherstack.com/current?access_key={os.getenv('WEATHER_STACK_API_KEY')}&query={city.lower()}"

    res = requests.get(url=url)

    return res.json()


llm = OllamaLLM(model="gemma3:4b")

# Step 2: Pull the ReAct prompt from langchain hub
prompt = hub.pull("hwchase17/react")

# Step 3: Create the ReAct agent manually with the pulled prompt
agent = create_react_agent(
    llm=llm, tools=[search_tool, get_weather_data], prompt=prompt
)

# Step 4: Wrap it up with AgentExecutor
agent_executor = AgentExecutor(
    agent=agent, tools=[search_tool, get_weather_data], verbose=True
)

# Step 5: Invoke
response = agent_executor.invoke(
    {
        "input": "Find the capital of Karnataka, and then find the current temperature of it"
    }
)

print(response)
