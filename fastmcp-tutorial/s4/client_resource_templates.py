import asyncio
from fastmcp import Client


async def main():

    client = Client("./server_resource_templates.py")

    async with client:
        res = await client.read_resource("users://alice/summary")
        print("Alice Summary")
        print(res[0].text)
        print()

        print("Bob Summary")
        res = await client.read_resource("users://bob/summary")
        print(res[0].text)
        print()

        # Simple one-segment wildcard
        res = await client.read_resource("logs://auth/error.log")
        print("Auth error log")
        print(res[0].text)
        print()

        # Multi-segment wildcard
        res = await client.read_resource("logs://auth/2026/05/error.log")
        print("Auth dated error log")
        print(res[0].text)
        print()

        # Deeper Hierarchy
        res = await client.read_resource("logs://payments/2026/05/31/transactions.log")
        print("Payment Transaction log")
        print(res[0].text)
        print()

        print("\n ------ Query Parameters ------- \n")  # For optional parameters

        res = await client.read_resource("greet://alice")
        print(res)
        print()

        res = await client.read_resource("greet://alice?language=es")
        print(res)
        print()

        res = await client.read_resource("greet://alice?language=fr")
        print(res)
        print()


if __name__ == "__main__":
    asyncio.run(main())
