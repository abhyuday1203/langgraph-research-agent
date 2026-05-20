from typing import TypedDict, Annotated, List, Optional
from langchain_core.messages import BaseMessage
import operator

class ResearchState(TypedDict):
    topic: str
    messages: Annotated[List[BaseMessage], operator.add]
    research_notes: str
    draft: str
    critique: str
    score: int
    iteration: int
    stage: str
    final_report: str
    next: Optional[str]
