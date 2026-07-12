"""server tools"""

from fastmcp import FastMCP

mcp = FastMCP("server-tools")


@mcp.tool
async def get_products(query: str) -> list[dict]:
    """Function to retrieve available products from an online store"""
    return [
        {"id": 1, "name": "Shoes"},
        {"id": 2, "name": "Shirts"},
    ]


if __name__ == "__main__":
    mcp.run()
