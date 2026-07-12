from fastmcp import Client
import asyncio


async def main():
    client = Client("./server_output_schema.py")

    async with client:
        tools = await client.list_tools()

        for tool in tools:
            print(f"\n --------------- {tool.name} --------------- ")
            print("Output Schema")
            print(tool.outputSchema)


if __name__ == "__main__":
    asyncio.run(main())
