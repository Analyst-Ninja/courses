from fastmcp import Client
import asyncio


async def main():
    client = Client("./server_arguments.py")

    async with client:
        result = await client.get_prompt(
            "build_search_query", {"query": "error logs", "limit": 15}
        )

        print(result)
        print("\n ------- build_search_query ------- \n")
        for msg in result.messages:
            print(f"{msg.role}: {msg.content}")


if __name__ == "__main__":
    asyncio.run(main())
