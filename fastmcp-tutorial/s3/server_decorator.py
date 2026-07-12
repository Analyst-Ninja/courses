from fastmcp import FastMCP

mcp = FastMCP("server-basics")


@mcp.tool(
    name="find_product",
    description="Retrieve products based on query",
    tags={"products", "catalog"},
    icons=[],
    meta={"version": "0.5", "author": "catalog-management"},
)
async def get_products(query: str) -> list[dict]:
    """Function to retrieve available products from an online store"""
    return [
        {"id": 1, "name": "Shoes"},
        {"id": 2, "name": "Shirts"},
    ]


if __name__ == "__main__":
    mcp.run()
