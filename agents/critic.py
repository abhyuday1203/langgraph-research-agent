import re
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage
from graph.state import ResearchState

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

async def critic_node(state: ResearchState) -> dict:
    draft = state["draft"]
    topic = state["topic"]

    prompt = f"""You are a strict editor reviewing a report on '{topic}'.

Report:
---
{draft}
---

Evaluate on:
- accuracy
- clarity
- structure
- completeness

Respond in EXACTLY this format:

SCORE: <integer 0 to 10>

FEEDBACK:
- bullet point 1
- bullet point 2
- bullet point 3
"""
    response = await llm.ainvoke([HumanMessage(content = prompt)])
    content = response.content
    score = 5
    score_match = re.search(r"SCORE:\s*(\d+)", content)
    if score_match:
        score = min(10, max(0, int(score_match.group(1))))

    feedback = content

    feedback_match = re.search(r"FEEDBACK:(.*)", content, re.DOTALL)

    if feedback_match:
        feedback = feedback_match.group(1).strip()

    print (f"[Critic] Score: {score}/10")

    return{
        "score": score,
        "critique": feedback,
        "stage": "reviewed",
        "messages": [
            AIMessage(content=f"Score: {score}/10")
        ]

    }

