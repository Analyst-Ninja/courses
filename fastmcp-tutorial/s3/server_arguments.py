from fastmcp import FastMCP
from typing import Annotated
from pydantic import Field
from mcp.types import Icon

mcp = FastMCP("server-basics")


@mcp.tool(
    name="find_product",
    description="Retrieve products based on query",
    tags={"products", "catalog"},
    icons=[Icon(src="")],
    meta={"version": "0.5", "author": "catalog-management"},
)
async def get_products(query: Annotated[str, "Query String"]) -> list[dict]:
    """Function to retrieve available products from an online store"""
    return [
        {"id": 1, "name": "Shoes"},
        {"id": 2, "name": "Shirts"},
    ]


@mcp.tool()
async def place_order(
    id: int,
    quantity=Field(5, description="quantity of product to be ordered", ge=3, le=10),
):
    return f"Order with id: {id} successfully placed for {quantity} items"


if __name__ == "__main__":
    mcp.run()
