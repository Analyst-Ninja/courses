"""get products"""

from fastmcp import Client
import asyncio


async def main():
    """get products"""
    client = Client("./server_tools.py")

    async with client:
        result = await client.call_tool("get_products", {"query": ""})
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
