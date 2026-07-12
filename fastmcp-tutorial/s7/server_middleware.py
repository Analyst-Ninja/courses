from fastmcp import FastMCP
from fastmcp.server.middleware import Middleware, MiddlewareContext
import sys

from fastmcp.server.middleware.middleware import CallNext
from fastmcp.tools.base import ToolResult
from mcp.types import CallToolRequestParams


def log(msg: str):
    print(msg, file=sys.stderr, flush=True)


class MiddlewareA(Middleware):

    async def on_call_tool(self, context: MiddlewareContext, call_next):
        log("--> Middleware A (before)")
        result = await call_next(context)
        log("--> Middleware A (after)")
        return result


class MiddlewareB(Middleware):

    async def on_call_tool(self, context: MiddlewareContext, call_next):
        log("--> Middleware B (before)")
        result = await call_next(context)
        log("--> Middleware B (after)")
        return result


class MiddlewareC(Middleware):

    async def on_call_tool(self, context: MiddlewareContext, call_next):
        log("--> Middleware C (before)")
        result = await call_next(context)
        log("--> Middleware C (after)")
        return result


mcp = FastMCP("Middleware demo server")

mcp.add_middleware(MiddlewareA())
mcp.add_middleware(MiddlewareB())
mcp.add_middleware(MiddlewareC())


@mcp.tool
async def greet(name: str) -> str:
    log(f"*** Tool handler executing: greet({name}) ***")
    return f"Hello, {name}"


if __name__ == "__main__":
    mcp.run()
