from fastmcp import Client
import asyncio


async def call_and_print(client: Client, name, args):
    print(f"\n ---------- Tool Call: {name}, {args}")

    try:
        result = await client.call_tool(name, args)
        print("Result: ", result.data)

    except Exception as e:
        print("Error Type: ", type(e).__name__)
        print(e.args[0])


async def main():
    client = Client("./server_error_handling.py")

    async with client:
        # result = await client.call_tool("divide", {"a": 1, "b": 0})
        # print(result)

        # result = await client.call_tool("divide", {"a": 1, "b": 2})
        # print(result)

        # Valid Call
        await call_and_print(client, "divide", {"a": 1, "b": 7})

        # Tool Error (Divide by zero not allowed)
        await call_and_print(client, "divide", {"a": 1, "b": 0})

        # Schema Validation Error (Non-numeric inputs)
        await call_and_print(client, "divide", {"a": "hello", "b": "world"})


if __name__ == "__main__":
    asyncio.run(main())
