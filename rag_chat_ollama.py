from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are sarcastical comedian assistant. You will help respond to queries in that fashion!"),
        ("user", "Question:{question}")
    ]
)

st.title('Langchain Demo with Llama 3.2 3b')

input_text = st.text_input("Search the topic you want")
llm = ChatOllama(model="llama2")
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))