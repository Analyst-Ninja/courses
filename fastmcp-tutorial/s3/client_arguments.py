"""get products"""

from fastmcp import Client
import asyncio
from pprint import pprint


async def main():
    """get products"""
    client = Client("./server_arguments.py")

    async with client:
        result = await client.call_tool("find_product", {"query": ""})
        pprint(result.content)

        result = await client.call_tool("place_order", {"id": 1, "quantity": 10})
        pprint(result.content)


if __name__ == "__main__":
    asyncio.run(main())
