from fastmcp import FastMCP
from fastmcp.exceptions import ToolError

mcp = FastMCP("server_error_handling")


@mcp.tool()
async def divide(a: float, b: float) -> float:

    if b == 0:
        raise ToolError("Division by zero is not allowed")

    return a / b


if __name__ == "__main__":
    mcp.run()
