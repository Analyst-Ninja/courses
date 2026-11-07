from ddgs import DDGS
from google.adk.agents import Agent
from google.adk.models import LiteLlm

model = LiteLlm(model="ollama_chat/qwen3.5:0.8b", api_base="http://localhost:11434")


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

    except Exception as e:  # noqa: BLE001
        return {
            "status": "error",
            "message": str(e),
        }


news_analyst = Agent(
    name="news_analyst",
    model=model,
    description="News analyst agent",
    instruction="""
    You are a helpful assistant that can analyze news articles and provide a summary of the news.

    When asked about news, you should use the google_search tool to search for the news.

    If the user ask for news using a relative time, you should use the get_current_time tool to get the current time to use in the search query.
    """,
    tools=[duckduckgo_search],
)
