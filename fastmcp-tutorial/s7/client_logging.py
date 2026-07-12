from fastmcp import Client
import asyncio


async def main():
    client = Client("./server_logging.py")

    async with client:
        res = await client.call_tool("add", {"a": 5, "b": 10})
        print(res)


if __name__ == "__main__":
    asyncio.run(main())
