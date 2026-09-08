# 📄 AI Study Assistant

An interactive Streamlit application that lets users upload a PDF and ask questions about its content. The app uses retrieval-augmented generation (RAG) to extract text, split it into searchable chunks, retrieve the most relevant sections, and generate an answer with an OpenAI language model.

## ✨ Features

- Upload PDF documents through a simple Streamlit interface
- Extract text from PDFs with `pdfminer.six`
- Split documents into overlapping chunks for more effective retrieval
- Create vector embeddings using Hugging Face's `all-MiniLM-L6-v2` model
- Store and search document chunks with ChromaDB
- Ask questions, request explanations, or generate quiz questions
- Display answers directly in the web application

## 🧠 How It Works

```text
PDF upload
    ↓
Text extraction
    ↓
Document chunking
    ↓
Hugging Face embeddings
    ↓
Chroma vector database
    ↓
Relevant context retrieval
    ↓
OpenAI-generated answer
```

The application follows a retrieval-augmented generation workflow. Instead of sending the entire PDF to the language model, it retrieves the most relevant text chunks and uses those chunks as context for the answer.

## 🛠️ Technologies Used

- Python
- Streamlit
- LangChain
- OpenAI API
- Hugging Face Sentence Transformers
- ChromaDB
- pdfminer.six
- Jupyter Notebook for experimentation and development

## 📁 Project Structure

```text
AI-Student-Assistant/
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
```

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/RShruthiCS/AI-Student-Assistant.git
cd AI-Student-Assistant
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows, activate it with:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your OpenAI API key

Do not commit an API key directly in `app.py`. Create a `.streamlit/secrets.toml` file:

```toml
OPENAI_API_KEY = "your_openai_api_key_here"
```

Make sure `.streamlit/secrets.toml` is included in `.gitignore`.

Update `app.py` to load the key securely:

```python
OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
```

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser. Upload a PDF and enter a question such as:

- `Summarize this document.`
- `Explain the main concepts in simple terms.`
- `Give me 5 quiz questions based on this PDF.`

## 📦 Example `requirements.txt`

```text
streamlit
pdfminer.six
langchain-core
langchain-text-splitters
langchain-huggingface
langchain-community
langchain-openai
chromadb
sentence-transformers
openai
```


## 🔮 Potential Improvements

- Preserve chat history for follow-up questions
- Add document summarization and flashcard-generation modes
- Support multiple uploaded PDFs
- Add input validation and file-size limits
- Deploy the application with Streamlit Community Cloud

## 👩‍💻 Author

**Shruthi Raghavan**  

- GitHub: [RShruthiCS](https://github.com/RShruthiCS)
- LinkedIn: [Shruthi Raghavan](https://www.linkedin.com/in/shruthi-raghavan04/)g
