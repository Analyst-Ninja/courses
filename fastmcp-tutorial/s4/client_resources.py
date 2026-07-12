import asyncio
from fastmcp import Client


async def main():
    client = Client("./server_resources.py")

    async with client:
        resources = await client.list_resources()
        print([r.uri for r in resources])

        print("\n ------------------ \n")
        config = await client.read_resource("data://config")
        print(config)
        print("\n ------------------ \n")
        print(config[0].text)


if __name__ == "__main__":
    asyncio.run(main())
