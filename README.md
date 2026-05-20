**AI Multi-Agent Research System**

> Production-grade AI multi-agent orchestration system built with LangGraph, Streamlit, Groq, and Tavily.

🌐 **Live Demo:**  
https://langgraph-research-agent-sanjfotwepthyyxadgczyc.streamlit.app/

![Python](https://img.shields.io/badge/Python-3.11-blue)
![LangGraph](https://img.shields.io/badge/LangGraph-Agent%20Workflow-black)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![Groq](https://img.shields.io/badge/LLM-Groq-orange)
![License](https://img.shields.io/badge/License-MIT-green)
A production-style multi-agent AI research backend built using:

- LangGraph
- FastAPI
- Groq LLMs
- Tavily Search
- Async orchestration

**Features**

- Multi-agent workflow
- Supervisor orchestration
- Web research agent
- Report writer agent
- Critic/reviewer agent
- Iterative improvement loop
- FastAPI backend
- JSON API responses

 **Architecture**

Streamlit → LangGraph → Supervisor Agent → Researcher / Writer / Critic

**How It Works**

1. The user sends a research topic through the FastAPI endpoint.
2. LangGraph initializes the workflow.
3. The Supervisor agent decides which specialized agent runs next.
4. The Researcher agent gathers information using Tavily Search.
5. The Writer agent generates a structured report.
6. The Critic agent evaluates report quality and assigns a score.
7. If the score is too low, the report is revised iteratively.
8. The final report is returned as JSON.


**Setup**

**1. Clone repo**

```bash
git clone <repo-url>
cd research-agent
```

**2. Create virtual environment**

```bash
python -m venv venv
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Create `.env`**

```env
GROQ_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
```

**5. Run server**

```bash
uvicorn api.main:app --reload
```


