from fastmcp import Client
import asyncio


async def main():
    client = Client("./server_state.py")

    async with client:
        print(await client.call_tool("start_session", {}))
        print(await client.call_tool("visit", {}))
        print(await client.call_tool("visit", {}))
        print(await client.call_tool("end_session", {}))


if __name__ == "__main__":
    asyncio.run(main())
