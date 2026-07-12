from fastmcp import FastMCP
import json

mcp = FastMCP(name="User Server")


@mcp.resource(uri="users://{user_id}/summary")
async def get_user_summary(user_id: str) -> str:
    """Return a basic summary of a user"""
    return json.dumps(
        {
            "user_id": user_id,
            "display_name": f"User {user_id}",
            "account_status": "active",
            "plan": "free",
        }
    )


@mcp.resource(uri="logs://{service}/{log_path*}")
async def get_log_entry(service: str, log_path: str) -> str:
    """Retrieve log content for a given service and log file path"""
    return json.dumps(
        {
            "service": service,
            "log_path": log_path,
            "message": f"Log data for {service}/{log_path}",
        }
    )


@mcp.resource(uri="greet://{name}{?language}")
async def greet(name: str, language: str = "en"):
    """Returns a greeting for a person"""
    if language == "es":
        return f"Hola, {name}"
    elif language == "fr":
        return f"Bonjour, {name}"
    else:
        return f"Hello, {name}"


if __name__ == "__main__":
    mcp.run()
