import os
from dotenv import load_dotenv

from langchain_community.llms.ollama import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

langchain_api_key = os.getenv("LANGCHAIN_API_KEY")
langchain_project = os.getenv("LANGCHAIN_PROJECT")

if langchain_api_key:
    os.environ["LANGCHAIN_API_KEY"] = langchain_api_key
if langchain_project:
    os.environ["LANGCHAIN_PROJECT"] = langchain_project
os.environ["LANGCHAIN_TRACING_V2"] = "true"

## Prompt Template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the question asked."),
        ("user","Question:{question}")
    ]
)

## streamlit framework
st.title("Langchain Demo With LLMA3.2")
input_text=st.text_input("What question you have in mind?")

## Ollama Llama3 Model 
llm=Ollama(model="llama3.2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))