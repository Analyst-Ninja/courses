from fastmcp import Client
import asyncio
import base64


async def main():
    client = Client("./server_dynamic_resources.py")

    async with client:
        # get active connections
        result = await client.read_resource("data://active-connections")
        print(result)
        print()

        # get current server datetime
        result = await client.read_resource("data://server-time")
        print(result)
        print()

        # Welcome message in bytes
        result = await client.read_resource("data://welcome-bytes")
        blob = result[0].blob
        print("Welcome bytes resource (raw)")
        print(blob)
        print()

        print("Welcome bytes decoded:")
        print(base64.b64decode(blob))


if __name__ == "__main__":
    asyncio.run(main())
