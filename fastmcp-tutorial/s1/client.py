"""
This is a simple client that connects to the FastMCP server and calls the `say_hello` method with the name "Alice". The result is printed to the console.
"""

import asyncio
from fastmcp import Client


async def main():
    """Main function to run the client."""
    client = Client("./server.py")

    async with client:
        result = await client.call_tool("say_hello")
        print(result.data)


if __name__ == "__main__":
    asyncio.run(main())
