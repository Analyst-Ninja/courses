from fastmcp import Client
import asyncio


async def main():
    client = Client("./server_return_types.py")

    async with client:
        res = await client.get_prompt(
            "clarification_request", {"topic": "deployment strategy"}
        )

        print("\n ------------- Clarification Request ------------- \n")
        for msg in res.messages:
            print(f"{msg.role} : {msg.content}")

        res = await client.get_prompt(
            "design_feedback", {"component": "Authenticatio Flow"}
        )

        print("\n ------------- Design Feedback ------------- \n")
        for msg in res.messages:
            print(f"{msg.role} : {msg.content}")

        print("\n Metadata: ", res.meta)


if __name__ == "__main__":
    asyncio.run(main())
