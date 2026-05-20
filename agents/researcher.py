import os
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage
from graph.state import ResearchState
from tools.search import search_tool

print("GROQ KEY EXISTS:", bool(os.getenv("GROQ_API_KEY")))

llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0)

async def researcher_node(state: ResearchState) -> dict:

   topic = state["topic"]
   print(f"[Researcher] Searching for: {topic}")

   search_results = await search_tool.ainvoke(topic)
   prompt = f"""You are a research assistant.Summarise the following search results 
   on the topic:{topic}'.

   Write clear, factual bullet points. Include key facts, dates, and statistics.
   Keep it under 500 words.

   Search results:
   {search_results}
   """
   response = await llm.ainvoke([HumanMessage(content=prompt)])

   print(f"[Researcher] Done.")

   return {
       "research_notes": response.content,
       "messages": [
           HumanMessage(content=f"Research topic: {topic}"),
           AIMessage(content=response.content)
       ]
   }

