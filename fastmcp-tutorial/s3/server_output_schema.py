from fastmcp import FastMCP
from dataclasses import dataclass
from pydantic import BaseModel

mcp = FastMCP("server-structured-output")


@dataclass
class User:
    id: int
    name: str


class UserModel(BaseModel):
    id: int
    name: str


@mcp.tool()
async def add(a: int, b: int) -> int:
    return a + b


@mcp.tool()
async def get_user() -> User:
    return User(id=1, name="Alice")


@mcp.tool()
async def get_user_model() -> UserModel:
    return UserModel(id=2, name="Bob")


if __name__ == "__main__":
    mcp.run()
