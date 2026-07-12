from fastmcp import FastMCP
from fastmcp.prompts import Message, PromptResult

mcp = FastMCP("DemoPromptServer")


@mcp.prompt
async def clarification_request(topic: str) -> list[Message]:
    """Ask the user to clarify a topic."""
    return [
        Message(
            f"Can you clarify what do you mean by '{topic}'? "
            "Please include context and constraints"
        )
    ]


@mcp.prompt
async def design_feedback(component: str) -> PromptResult:
    """Request structured design feedback."""
    return PromptResult(
        messages=[
            Message(
                f"Provide design feedback for the '{component}'."
                "Focus on unsability and maintainability."
            ),
            Message(
                f"I will analyse the design and give detailed feedback",
                role="assistant",
            ),
        ],
        meta={"category": "design review", "priority": "medium"},
    )


if __name__ == "__main__":
    mcp.run()
