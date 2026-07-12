from fastmcp import FastMCP
from fastmcp.dependencies import CurrentContext
from fastmcp.server.context import Context

mcp = FastMCP("State demo server")


@mcp.tool
async def start_session(ctx: Context = CurrentContext()) -> str:
    """Initialize the sessio state"""
    await ctx.set_state("username", "Alice")
    await ctx.set_state("visits", 1)
    return "Session Started"


@mcp.tool
async def visit(ctx: Context = CurrentContext()) -> str:
    """Read and update the session state accross requests"""

    username = await ctx.get_state("username")
    visits = await ctx.get_state("visits") or 0

    visits += 1
    await ctx.set_state("visits", visits)

    return f"{username} has visited {visits} times."


@mcp.tool
async def end_session(ctx: Context = CurrentContext()) -> str:
    username = await ctx.get_state("username")
    visits = await ctx.get_state("visits")

    await ctx.delete_state(username)
    await ctx.delete_state(visits)

    return f"Session ended for {username} after {visits} visits."


if __name__ == "__main__":
    mcp.run()
