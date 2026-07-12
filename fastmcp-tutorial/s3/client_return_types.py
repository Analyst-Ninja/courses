from fastmcp import Client
import asyncio


async def main():

    client = Client("./server_return_types.py")

    async with client:
        print("\n", "=" * 40, "get_info", "=" * 40)
        result = await client.call_tool("get_info")
        print(result)

        print("\n", "=" * 40, "get_info", "=" * 40)
        result = await client.call_tool("get_sum")
        print(result)

        print("\n", "=" * 40, "get_info", "=" * 40)
        result = await client.call_tool("get_chart")
        for item in result.content:
            # print(item)
            print(type(item).__name__)

        print("\n", "=" * 40, "get_info", "=" * 40)
        result = await client.call_tool("get_sum2")
        print(result)

        print("\n", "=" * 40, "get_info", "=" * 40)
        result = await client.call_tool("get_chart_dict")
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
