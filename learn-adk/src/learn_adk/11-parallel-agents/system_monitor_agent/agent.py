"""
System Monitor Root Agent

Workflow graph: fan out to CPU/memory/disk agents in parallel, join, then
synthesize one report.
"""

from google.adk.workflow import END, START, JoinNode, Workflow

from .subagents.cpu_info_agent.agent import cpu_info_agent
from .subagents.disk_info_agent.agent import disk_info_agent
from .subagents.memory_info_agent.agent import memory_info_agent
from .subagents.synthesizer_agent.agent import system_report_synthesizer

# Waits for all three gatherers before the synthesizer runs.
gather_join = JoinNode(name="gather_join")

root_agent = Workflow(
    name="system_monitor_agent",
    edges=[
        (
            START,
            (cpu_info_agent, memory_info_agent, disk_info_agent),  # fan-out
            gather_join,  # fan-in
            system_report_synthesizer,
            END,
        ),
    ],
)
