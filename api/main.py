import json
from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from graph.builder import build_graph


app = FastAPI(title="Research Agent API")

graph = build_graph()

class ResearchRequest(BaseModel):
    topic: str

@app.post("/research")
async def run_research(request: ResearchRequest):
    result = await graph.ainvoke({
        "topic": request.topic,
        "iteration": 0,
        "stage": ""
    })
    return {
        "topic": request.topic,
        "report": result["final_report"],
        "score": result.get("score", 0),
        "iterations": result.get("iteration", 0)
    }

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def home():
    return {
        "message": "AI Research Agent API is running"
    }



