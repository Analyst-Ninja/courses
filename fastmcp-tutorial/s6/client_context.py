from fastmcp import Client
import asyncio


async def main():
    client = Client("./server_context.py")
    async with client:
        await client.call_tool("greet", {"name": "Alice"})


if __name__ == "__main__":
    asyncio.run(main())
