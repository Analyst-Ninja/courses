import asyncio
from fastmcp import Client


async def main():

    client = Client("./server_middleware.py")

    async with client:
        result = await client.call_tool("greet", {"name": "Alice"})
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
