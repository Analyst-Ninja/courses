from fastmcp import Client
import asyncio


async def main():
    client = Client("./server_structured_output.py")

    async with client:
        print("\n---------- add ---------")
        result = await client.call_tool("add", {"a": 3, "b": 5})
        print(result, "\n")

        print("\n---------- get user ---------")
        result = await client.call_tool("get_user")
        print(result, "\n")

        print("\n---------- get user model ---------")
        result = await client.call_tool("get_user_model")
        print(result, "\n")


if __name__ == "__main__":
    asyncio.run(main())
