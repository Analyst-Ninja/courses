from fastmcp import FastMCP
from fastmcp.exceptions import ResourceError

mcp = FastMCP(name="ErrorDemoServer", mask_error_details=True)


@mcp.resource(uri="demo://python-error")
async def python_error() -> str:
    """Demonstrate a standard Python exception"""
    raise ValueError("Something went wrong internally")


@mcp.resource(uri="demo://resource-error")
async def resource_error() -> str:
    """Demonstrate a ResourceError with a controlled message"""
    raise ResourceError("Requested item was not found")


if __name__ == "__main__":
    mcp.run()
