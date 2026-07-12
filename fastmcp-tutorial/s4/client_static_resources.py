import asyncio
from fastmcp import Client
import yaml
from pprint import pprint


async def main():
    client = Client("./server_static_resources.py")

    async with client:
        # Text Resource
        result = await client.read_resource("resource://hello")
        print(f"\n {result} \n")

        # Binary Resource
        result = await client.read_resource("resource://binary")
        print(f"\n {result} \n")

        # File Resource
        result = await client.read_resource("resource://file")
        data = yaml.safe_load(result[0].text)
        pprint(f"\n {type(data)} \n")
        pprint(data)

        # # HTTP Resource
        # result = await client.read_resource("resource://site")
        # print(f"\n {result}")

        # Directory Resource
        result = await client.read_resource("resource://data")
        print(f"\n{result}")


if __name__ == "__main__":
    asyncio.run(main())
