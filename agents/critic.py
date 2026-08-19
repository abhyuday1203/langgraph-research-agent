import re
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage
from graph.state import ResearchState

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    reasoning_effort="low"
)

async def critic_node(state: ResearchState) -> dict:
    draft = state["draft"]
    topic = state["topic"]

    prompt = f"""Review this report on '{topic}'.

Report:
---
{draft}
---

Evaluate:
- accuracy
- clarity
- structure
- completeness

Respond ONLY with:

SCORE: <integer 0 to 10>

FEEDBACK:
- one concise issue
- one concise issue
- one concise issue
"""

    response = await llm.ainvoke([HumanMessage(content=prompt)])

    content = response.content
    score = 5

    score_match = re.search(r"SCORE:\s*(\d+)", content)
    if score_match:
        score = min(10, max(0, int(score_match.group(1))))

    feedback = content
    feedback_match = re.search(r"FEEDBACK:(.*)", content, re.DOTALL)

    if feedback_match:
        feedback = feedback_match.group(1).strip()

    print(f"[Critic] Score: {score}/10")

    return {
        "score": score,
        "critique": feedback,
        "stage": "reviewed",
        "messages": [
            AIMessage(content=f"Score: {score}/10")
        ]
    }
