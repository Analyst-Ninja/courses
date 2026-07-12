from fastmcp import Client
import asyncio


async def main():
    client = Client("./server_prompts.py")

    async with client:
        greeting = await client.get_prompt(
            "write_greeting", {"name": "Alice", "tone": "casual"}
        )
        print(greeting)
        print()

        farewell = await client.get_prompt("write_farewell", {"name": "Alice"})
        print(farewell)
        print()


if __name__ == "__main__":
    asyncio.run(main())
