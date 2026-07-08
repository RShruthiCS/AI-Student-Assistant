import streamlit as st
from pdfminer.high_level import extract_text
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
import tempfile
import os

OPENAI_API_KEY = "your_openai_api_key_here"
def build_pipeline(pdf_path):
    # Extract text
    raw_text = extract_text(pdf_path)
    
    # Wrap in Document
    documents = [Document(page_content=raw_text)]
    
    # Chunk
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_documents(documents)
    
    # Embed and store
    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )
    vectordb = Chroma.from_documents(chunks, embedding)
    
    # LLM
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        api_key=OPENAI_API_KEY,
        temperature=0
    )
    
    retriever = vectordb.as_retriever(search_kwargs={"k": 4})
    return llm, retriever

def ask(llm, retriever, question):
    docs = retriever.invoke(question)
    context = "\n\n".join([d.page_content for d in docs])
    response = llm.invoke(
        f"You are a helpful study assistant. Use the context below to answer the question. "
        f"You can also generate quizzes or explain concepts if asked.\n\n"
        f"Context:\n{context}\n\nQuestion: {question}"
    )
    return response.content


# ── Streamlit UI ────────────────────────────────────────────
st.set_page_config(page_title="PDF Study Assistant", page_icon="📄")
st.title("📄 PDF Study Assistant")
st.markdown("Upload any PDF and ask questions, get explanations, or request a quiz!")

uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    with st.spinner("Reading and indexing your PDF..."):
        try:
            llm, retriever = build_pipeline(tmp_path)
            st.session_state.llm = llm
            st.session_state.retriever = retriever
            st.success(f"✅ {uploaded_file.name} indexed! Ask anything.")
        except Exception as e:
            st.error(f"Error: {e}")
        finally:
            os.unlink(tmp_path)

if "llm" in st.session_state:
    question = st.text_input(
        "Ask a question",
        placeholder="e.g. Explain RAG, Give me 3 quiz questions, Summarize this"
    )
    if question:
        with st.spinner("Thinking..."):
            answer = ask(
                st.session_state.llm,
                st.session_state.retriever,
                question
            )
        st.markdown("### Answer")
        st.write(answer)