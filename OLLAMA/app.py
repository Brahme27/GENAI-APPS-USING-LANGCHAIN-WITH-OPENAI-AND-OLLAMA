# Import the 'os' module to interact with the operating system
import os 

from dotenv import load_dotenv

from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

# Langsmith tracing configuration
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

## prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the question asked."),
    ("user", "question: {question}"),
])


## Streamlit app
st.title("GenAi App using Langchain with Ollama deepSeek R1 model")
input_text = st.text_input("Enter your question here:")


## Calling Ollama deepSeek R1 model

llm=Ollama(model="deepseek-r1")
output_parser=StrOutputParser()
chain=prompt | llm | output_parser


if input_text:
    st.write(chain.invoke({"question": input_text}))
