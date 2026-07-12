"""
This is the server code for the FastMCP example. It defines a FastMCP application and runs it.
"""

from fastmcp import FastMCP

mcp = FastMCP()


@mcp.tool
def say_hello() -> str:
    """A simple tool that returns a greeting message."""
    return "Hello World!!!!"


if __name__ == "__main__":
    mcp.run()
