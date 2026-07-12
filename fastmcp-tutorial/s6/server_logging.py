from fastmcp import FastMCP
from fastmcp.server.context import Context
from fastmcp.dependencies import CurrentContext

mcp = FastMCP("Logging demo server")


@mcp.tool
async def compute_sum(numbers: list[int], ctx: Context = CurrentContext()) -> int:
    await ctx.debug("compute_sum called")
    await ctx.info(f"received {len(numbers)} numbers")

    total = 0
    for i, n in enumerate(numbers):
        await ctx.debug(f"Adding number", extra={"idenx": i, "value": n})
        total += n

    await ctx.info("Computation Complete", extra={"result": total})

    return total


if __name__ == "__main__":
    mcp.run()
