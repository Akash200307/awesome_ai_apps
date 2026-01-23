from dotenv import load_dotenv
from llama_index.llms import groq
from llama_index.embeddings import huggingface
from llama_index.core import VectorStoreIndex,SimpleDirectoryReader
from llama_index.core import Settings
import streamlit as st
load_dotenv()

st.set_page_config(page_title="RAG with Groq + LlamaIndex",layout='wide')
st.title("Upload files -> Ask questions")
llm=groq.Groq(model='moonshotai/kimi-k2-instruct-0905')
embed=huggingface.HuggingFaceEmbedding(model_name='sentence-transformers/all-MiniLM-L6-v2')

Settings.llm=llm
Settings.embed_model=embed
documents=SimpleDirectoryReader('data').load_data()
index=VectorStoreIndex.from_documents(documents)
query_engine=index.as_query_engine()
user_query=st.text_input("Ask your questions?",placeholder="what is the context?")

if st.button("ask"):
    response=query_engine.query(user_query)
    st.write("**ANSWER**")
    st.write(response.response) # type: ignore

