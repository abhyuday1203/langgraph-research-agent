from graph.state import ResearchState


async def supervisor_node(state: ResearchState) -> dict:
    if not state.get("research_notes"):
        return {"next": "researcher"}

    if not state.get("draft"):
        return {"next": "writer"}

    stage = state.get("stage", "")
    score = state.get("score", 0)
    iteration = state.get("iteration", 0)

    print(f"[Supervisor] stage={stage}, score={score}, iteration={iteration}")

    if stage == "written":
        return {"next": "critic"}

    if stage == "reviewed":
        if score < 7 and iteration < 3:
            return {"next": "writer"}

        return {
            "next": "END",
            "final_report": state.get("draft", "")
        }

    return {"next": "END"}