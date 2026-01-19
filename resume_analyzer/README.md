# Resume Analyzer

This project demonstrates the use of LangChain agents and tools to build AI-powered assistants for various tasks, including weather information retrieval and knowledge base search.

## Features

- **Weather Assistant**: Uses Google Gemini (via LangChain) to answer weather queries, fetches real-time weather data, and locates user cities.
- **RAG Example**: Shows how to use a retrieval-augmented generation (RAG) agent with a small knowledge base about computers and fruits.
- **Modular Design**: Organized with reusable tools and context schemas.

## Project Structure

- `main.py` — Entry point (if present)
- `langchain/tuto.py` — Weather assistant using Gemini and custom tools
- `langchain/rag.py` — RAG agent with a small knowledge base
- `langchain/multimodalInput.py` — (Not described here)
- `pyproject.toml` — Project dependencies and configuration

## Setup

1. **Clone the repository**
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   # or, if using pyproject.toml
   pip install .
   ```
3. **Set up environment variables**:
   - Create a `.env` file with your API keys (for Google Gemini, Groq, etc.)

## Usage

### Weather Assistant

Run the weather assistant example:

```bash
python langchain/tuto.py
```

- The agent will use Gemini to answer weather questions, fetch weather data from wttr.in, and locate the user's city based on a user ID.

### RAG Example

Run the RAG agent example:

```bash
python langchain/rag.py
```

- The agent will answer questions about computers, laptops, Apple products, and fruits using a small in-memory knowledge base.

## Requirements

- Python 3.9+
- [LangChain](https://python.langchain.com/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [requests](https://pypi.org/project/requests/)
- [sentence-transformers](https://www.sbert.net/)
- [faiss-cpu](https://pypi.org/project/faiss-cpu/)
- [langchain-google-genai](https://pypi.org/project/langchain-google-genai/)
- [langchain-groq](https://pypi.org/project/langchain-groq/)
- [langchain-huggingface](https://pypi.org/project/langchain-huggingface/)

## Notes

- You must provide valid API keys for Gemini, Groq, or other LLM providers in your `.env` file.
- The weather tool uses the public [wttr.in](https://wttr.in/) API.

## License

MIT License
