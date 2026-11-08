"""
LinkedIn Post Generator Root Agent

Workflow graph: generate an initial post, then loop reviewer -> router -> refiner
until the reviewer approves the post or MAX_ITERATIONS is reached.
"""

from google.adk.agents import Context
from google.adk.workflow import START, Workflow

from .subagents.post_generator.agent import initial_post_generator
from .subagents.post_refiner.agent import post_refiner
from .subagents.post_reviewer.agent import post_reviewer

MAX_ITERATIONS = 10


def review_router(ctx: Context) -> None:
    """Decide whether to refine again or finish.

    Replaces LoopAgent's escalate/max_iterations logic: the reviewer's
    exit_loop tool sets state["review_passed"], and we count passes here.
    """
    iterations = ctx.state.get("loop_iterations", 0) + 1
    ctx.state["loop_iterations"] = iterations

    if ctx.state.get("review_passed") or iterations >= MAX_ITERATIONS:
        ctx.route = "done"
    else:
        ctx.route = "refine"


def finish(ctx: Context) -> str:
    """Terminal node: emit the approved post as the workflow output."""
    return ctx.state.get("current_post", "")


# Cycle: reviewer -> router -> (refine -> reviewer) | done -> finish
root_agent = Workflow(
    name="LinkedInPostGenerationPipeline",
    description="Generates and refines a LinkedIn post through an iterative review process",
    edges=[
        (START, initial_post_generator, post_reviewer, review_router),
        (review_router, {"refine": post_refiner, "done": finish}),
        (post_refiner, post_reviewer),
    ],
)
