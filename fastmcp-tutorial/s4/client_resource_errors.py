import asyncio
from fastmcp import Client


async def main():

    client = Client("./server_resource_errors.py")

    async with client:
        # Standard Python Exception
        try:
            res = await client.read_resource("demo://python-error")
            print(res)
        except Exception as e:
            print("Python error resource failed")
            print(e)
        print()

        # Resource Error Exception
        try:
            res = await client.read_resource("demo://resource-error")
            print(res)
        except Exception as e:
            print("Resource error resource failed")
            print(e)
        print()


if __name__ == "__main__":
    asyncio.run(main())
