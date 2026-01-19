from dotenv import load_dotenv
from llama_index.llms import groq
from llama_index.embeddings import huggingface
from llama_index.core import VectorStoreIndex,SimpleDirectoryReader
from llama_index.core import Settings
load_dotenv()


llm=groq.Groq(model='moonshotai/kimi-k2-instruct-0905')
embed=huggingface.HuggingFaceEmbedding(model_name='sentence-transformers/all-MiniLM-L6-v2')

Settings.llm=llm
Settings.embed_model=embed
documents=SimpleDirectoryReader('data').load_data()
index=VectorStoreIndex.from_documents(documents)


query_engine=index.as_query_engine()


print(query_engine.query("What is the population ?"))