from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
os.environ['LANGCHAIN_PROJECT'] = 'chatbot-01'
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = 'true'

#prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', 'You are a helpful assistant. Please answer the queries!'),
        ('user', 'Question:{question}')
    ]
)

#llm
llm = Ollama(model='phi3')

#chain
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

#streamlit
st.title('Chatbot with phi-3-mini')
input_text = st.text_input("search for any topic!")
if input_text:
    st.write(chain.invoke({'question':input_text}))
