"""MCP for weather station"""

from fastmcp import FastMCP
from mcp.types import Icon

mcp = FastMCP(
    name="server-basics",
    instructions="Use this server to get weather information for a specific day",
    version="0.1",
    icons=[Icon(src="https://cdn-icons-png.flaticon.com/128/16342/16342339.png")],
    website_url="website.com",
)


@mcp.tool
async def weather_lookup(city: str) -> str:
    """Return the current weather in a specifc city"""
    return f"The current weather in {city} is cloudy with a chance of meatballs"


@mcp.resource("resource://docs")
async def server_documentation() -> str:
    """Provides basic built-in documentation from the server"""
    return "The basic FastMCP server can expose tools, resource and prompts"


@mcp.prompt
async def text_summarization(topic: str) -> str:
    """Generic template hosted on the server that any client could use"""
    return f"Write a three-sentence summary about: {topic}"


if __name__ == "__main__":
    mcp.run()
    # mcp.run(transport="http", host="127.0.0.1", port=9000)
