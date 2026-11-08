"""
Sequential Agent with a Minimal Callback

This example demonstrates a lead qualification pipeline with a minimal
before_agent_callback that only initializes state once at the beginning.
"""

from google.adk.workflow import START, Workflow

from .subagents.recommender.agent import action_recommender_agent
from .subagents.scorer.agent import lead_scorer_agent
from .subagents.validator.agent import lead_validator_agent

# Tuple = chain of edges: START -> validator -> scorer -> recommender
root_agent = Workflow(
    name="LeadQualificationPipeline",
    description="A pipeline that validates, scores, and recommends actions for sales leads",
    edges=[
        (START, lead_validator_agent, lead_scorer_agent, action_recommender_agent),
    ],
)
