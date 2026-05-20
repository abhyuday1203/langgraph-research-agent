# AI Multi-Agent Research System

A production-style multi-agent AI research backend built using:

- LangGraph
- FastAPI
- Groq LLMs
- Tavily Search
- Async orchestration

## Features

- Multi-agent workflow
- Supervisor orchestration
- Web research agent
- Report writer agent
- Critic/reviewer agent
- Iterative improvement loop
- FastAPI backend
- JSON API responses

## Architecture

FastAPI → LangGraph → Supervisor → Researcher → Writer → Critic

## Setup

### 1. Clone repo

```bash
git clone <repo-url>
cd research-agent
```

### 2. Create virtual environment

```bash
python -m venv venv
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env`

```env
GROQ_API_KEY=your_key_here
TAVILY_API_KEY=your_key_here
```

### 5. Run server

```bash
uvicorn api.main:app --reload
```

## API Docs

Visit:

```plaintext
http://127.0.0.1:8000/docs
```