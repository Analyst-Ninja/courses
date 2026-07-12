from fastmcp import FastMCP
from fastmcp.dependencies import CurrentContext
from fastmcp.server.context import Context

mcp = FastMCP("Greetings Server")


@mcp.tool
async def greet(name: str, ctx: Context = CurrentContext()):
    await ctx.info(f"Greetings requested for the user: {name}")
    return f"Hello, {name}!"


if __name__ == "__main__":
    mcp.run()
