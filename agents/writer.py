from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage
from graph.state import ResearchState

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0.4)


async def writer_node(state: ResearchState) -> dict:
    topic = state["topic"]
    notes = state["research_notes"]
    critique = state.get("critique", "")
    iteration = state.get("iteration", 0)

    revision_context = ""

    if critique and iteration > 0:
        revision_context = f"""
A critic reviewed your previous draft and said:
---
{critique}
---

Incorporate this feedback.
"""

    prompt = f"""You are a professional report writer. Write a report on: '{topic}'.

Use these research notes:
---
{notes}
---

{revision_context}

Format with:
- Executive summary (2-3 sentences)
- 3-4 sections with headings
- A conclusion
"""

    response = await llm.ainvoke([HumanMessage(content=prompt)])

    print(f"[Writer] Draft written (iteration {iteration + 1})")

    return {
        "draft": response.content,
        "iteration": iteration + 1,
        "stage": "written",
        "messages": [
            AIMessage(content=f"Draft iteration {iteration + 1} done.")
        ]
    }

