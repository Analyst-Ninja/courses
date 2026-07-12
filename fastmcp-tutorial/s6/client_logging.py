from fastmcp import Client
from fastmcp.client.logging import LogMessage
import asyncio
import logging

logging.basicConfig(level=logging.DEBUG, format="%(message)s")

logger = logging.getLogger("mcp-client")


async def log_handler(message: LogMessage):
    msg = message.data.get("msg")
    extra = message.data.get("extra")
    level = message.level.upper()

    if extra:
        logger.info(f"[{level}] {msg} | extra={extra}")
    else:
        logger.info(f"[{level}] {msg}")


async def main():
    client = Client("./server_logging.py", log_handler=log_handler)

    async with client:
        res = await client.call_tool("compute_sum", {"numbers": [1, 2, 3, 4]})

        print(f"\nFINAL RESULT: {res}")


if __name__ == "__main__":
    asyncio.run(main=main())
