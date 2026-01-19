# Awesome AI Apps

Welcome to a creative playground for AI-powered applications! This workspace features hands-on experiments with LangChain, LlamaIndex, and custom tools for retrieval-augmented generation (RAG), multimodal input, and resume analysis.

## Project Structure & Highlights

### langchain_practice/

A suite of LangChain experiments:

- **dynamic_prompt.py**: Dynamically adapts prompts based on user roles (expert, child, etc.) using LangChain middleware.
- **dynamicmodel.py**: Switches between LLMs (Kimi, Llama) based on conversation length for cost-effective, context-aware responses.
- **main.py**: Simple hello-world script for LangChain setup.
- **multimodalInput.py**: Demonstrates multimodal input (text + image) with Google Gemini, encoding images for AI analysis.
- **rag.py**: RAG agent with a tiny knowledge base (computers, fruits), using FAISS for vector search and Groq for LLM.
- **small_rag.py**: RAG agent focused on facts about the Netherlands, with document loading and vector search.
- **tuto.py**: Weather assistant using Google Gemini, custom tools for weather/location, and context schemas.
- **resume_rag.faiss/** & **text.rag.faiss/**: FAISS vector stores for RAG experiments (binary index files).

### llamaIndex/

Experiments with LlamaIndex for RAG:

- **rag/small_rag.py**: Loads facts from data/rag.txt, builds a vector index, and answers queries about the Netherlands.
- **rag/data/rag.txt**: Knowledge base with facts about the Netherlands.

### resume_analyzer/

AI-powered resume analysis:

- **resume_analyzer.py**: Extracts text from resumes (PDF), builds a FAISS vector store, and enables semantic search over resume content.

### LLM/

Reserved for future large language model experiments.

## Getting Started

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   # or, if using pyproject.toml
   pip install .
   ```
2. **Configure environment variables**
   Create a `.env` file with your API keys (Google Gemini, Groq, etc.).

## Features

- Modular AI assistants and RAG agents
- Dynamic prompt and model selection
- Multimodal input (text + image)
- FAISS-powered vector search for knowledge bases and resumes
- Ready for experimentation and extension
