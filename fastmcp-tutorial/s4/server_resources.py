import json
from fastmcp import Context, FastMCP

mcp = FastMCP(name="Config Server")


@mcp.resource("data://config")
async def config() -> str:
    return json.dumps(
        {
            "version": "1.0",
            "features": ["tools", "resources"],
        }
    )


if __name__ == "__main__":
    mcp.run()
