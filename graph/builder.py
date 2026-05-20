from langgraph.graph import StateGraph, END
from graph.state import ResearchState
from agents.supervisor import supervisor_node
from agents.researcher import researcher_node
from agents.writer import writer_node
from agents.critic import critic_node

def build_graph():
    graph = StateGraph(ResearchState)

    graph.add_node("supervisor", supervisor_node)
    graph.add_node("researcher", researcher_node)
    graph.add_node("writer", writer_node)
    graph.add_node("critic", critic_node)

    graph.set_entry_point("supervisor")

    graph.add_conditional_edges(
        "supervisor",
        lambda state: state["next"],
        {
            "researcher": "researcher",
            "writer": "writer",
            "critic": "critic",
            "END": END

        }
    )

    graph.add_edge("researcher", "supervisor")
    graph.add_edge("writer", "supervisor")
    graph.add_edge("critic", "supervisor")

    return graph.compile()


