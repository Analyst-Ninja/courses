from ddgs import DDGS
from google.adk import Agent
from google.adk.models.lite_llm import LiteLlm


def duckduckgo_search(query: str) -> dict:
    """
    Search the web using DuckDuckGo.

    Args:
        query: Search query to execute.

    Returns:
        Search results with titles, URLs and snippets.
    """

    try:
        results = DDGS().text(
            query,
            max_results=5,
        )

        return {
            "status": "success",
            "query": query,
            "results": [
                {
                    "title": result.get("title"),
                    "url": result.get("href"),
                    "snippet": result.get("body"),
                }
                for result in results
            ],
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
        }


root_agent = Agent(
    name="tool_agent",
    model=LiteLlm(
        model="ollama_chat/qwen3.5:0.8b",  # "ollama_chat/" + model name from `ollama list`
        api_base="http://localhost:11434",
    ),
    description="Tool Agent",
    instruction="""
    You are a helpful assistant that can use the following tools:
    - duckduckgo_search
    """,
    tools=[duckduckgo_search],
)
