from fastmcp import FastMCP
from fastmcp.server.middleware.logging import LoggingMiddleware

mcp = FastMCP("LoggingMiddleware Demo Server")

mcp.add_middleware(LoggingMiddleware(include_payloads=True))


@mcp.tool
async def add(a: int, b: int) -> int:
    return a + b


if __name__ == "__main__":
    mcp.run()
