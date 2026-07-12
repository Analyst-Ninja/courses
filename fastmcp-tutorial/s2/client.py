from fastmcp import FastMCP
from fastmcp import Client
import asyncio


async def main():
    # server = FastMCP("In Memory Server")
    # client = Client(server)
    # print(client)

    client = Client("./server.py")

    async with client:
        print("Connected", client.is_connected())

        # call know tool
        w = await client.call_tool("weather_lookup", {"city": "London"})
        print("Tool:", w.data)

        # read all resources
        rs = await client.list_resources()
        for r in rs:
            content = await client.read_resource(r.uri)
            for block in content:
                print("Resource:", getattr(block, "text", block))

        # call prompt
        p = await client.get_prompt("text_summarization", {"topic": "tutorial"})
        print("Prompt:", p.messages)

    print("Connected after block:", client.is_connected())

    location = Client("./server_location.py")

    async with location:
        c = await location.call_tool("coordinates", {"city": "New York"})
        print("Location Coordinates:", c.data)


if __name__ == "__main__":
    asyncio.run(main=main())
