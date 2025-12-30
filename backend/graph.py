from langgraph.graph import StateGraph
from state import IncidentState

from agents.signal_analyzer import signal_analyzer
from agents.root_cause import root_cause_reasoner
from agents.fix_planner import fix_planner
from agents.safety_validator import safety_validator
from agents.executor import executor

graph = StateGraph(IncidentState)

graph.add_node("analyze", signal_analyzer)
graph.add_node("reason", root_cause_reasoner)
graph.add_node("plan", fix_planner)
graph.add_node("safety", safety_validator)
graph.add_node("execute", executor)

graph.set_entry_point("analyze")
graph.add_edge("analyze", "reason")
graph.add_edge("reason", "plan")
graph.add_edge("plan", "safety")
graph.add_edge("safety", "execute")

app = graph.compile()
