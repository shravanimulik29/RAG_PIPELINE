from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")
###prompt template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system" ,"You are a helpfull assistance please response to queries"),
        ("user","Question:{question}")
    ]
)

##streamlit function
st.title('Langchain Demo with openai api')
input_text=st.text_input("Search the topic u want")

#openai llm
llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))