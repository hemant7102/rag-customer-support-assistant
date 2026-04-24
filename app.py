import streamlit as st
import os
from src.graph_workflow import run_graph, initialize_db

st.set_page_config(page_title="AI Support", layout="wide")

st.title("🤖 AI Customer Support Assistant")

# -------- FILE UPLOAD --------
uploaded_file = st.file_uploader("📄 Upload your PDF", type="pdf")

if uploaded_file:
    file_path = os.path.join("knowledge_base", uploaded_file.name)
    os.makedirs("knowledge_base", exist_ok=True)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ File uploaded successfully!")

    if "db_initialized" not in st.session_state:
        initialize_db(file_path)
        st.session_state.db_initialized = True
        st.success("📚 Knowledge base ready!")

# -------- CHAT --------
if "chat" not in st.session_state:
    st.session_state.chat = []

query = st.chat_input("Ask your question...")

if query and "db_initialized" in st.session_state:
    result = run_graph(query, st.session_state.chat)

    st.session_state.chat.append({
        "user": query,
        "bot": result["response"],
        "confidence": result["confidence"],
        "sources": result["sources"],
        "escalated": result["needs_escalation"]
    })

# -------- DISPLAY --------
for chat in st.session_state.chat:
    with st.chat_message("user"):
        st.write(chat["user"])

    with st.chat_message("assistant"):
        st.write(chat["bot"])

        # 🔥 CONFIDENCE (FIXED)
        if chat["confidence"] == "HIGH":
            st.success("Confidence: HIGH")
        elif chat["confidence"] == "MEDIUM":
            st.warning("Confidence: MEDIUM")
        else:
            st.error("Confidence: LOW")

        # 🔥 ESCALATION
        if chat["escalated"]:
            st.error("⚠️ Escalated to human")

        # 🔥 CLEAN SOURCES
        if chat["sources"]:
            with st.expander("📄 Sources"):
                for i, src in enumerate(chat["sources"]):
                    st.write(f"{i+1}. {src}")