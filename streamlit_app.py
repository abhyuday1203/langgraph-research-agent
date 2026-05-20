import streamlit as st
import asyncio

from dotenv import load_dotenv

load_dotenv()

from graph.builder import build_graph

graph = build_graph()

st.set_page_config(
    page_title="AI Research agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Multi-Agent Research System")

st.markdown("""
Generate AI-powered research reports using:
 -Research agents
 -Writer agents
 -Critic Agents 
 -LangGraph orchestration
 """)

topic = st.text_input(
    "Enter a research topic:",
    placeholder="Impact of AI on software engineering jobs"
)

async def run_agent(topic: str):
    result = await graph.ainvoke({
        "topic": topic,
        "iteration": 0,
        "stage": ""
    })

    return result

if st.button("Generate Report"):

    if not topic.strip():
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Agents are researching and writing..."):

            result = asyncio.run(run_agent(topic))

            st.success("Report generated successfully!")

            col1, col2 = st.columns(2)

            with col1:
                    st.metric("Score", result["score"])

            with col2:
                    st.metric("Iterations", result["iteration"])

            st.markdown("## 📄 Generated Report")

            st.markdown(result["final_report"])


