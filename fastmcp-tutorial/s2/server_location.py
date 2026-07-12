"""City Location"""

from fastmcp import FastMCP

mcp = FastMCP("city-location")


@mcp.tool
async def coordinates(city: str) -> str:
    """Gives the coordinates of a specific city"""
    return f"Coordinates for {city}: lat=10.5, lon=20.0"


if __name__ == "__main__":
    mcp.run()
