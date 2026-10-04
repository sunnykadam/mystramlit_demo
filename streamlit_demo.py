import os
from langchain_openai import ChatOpenAI
import streamlit as st

NEW_KEY = os.getenv("NEW_KEY")

llm = ChatOpenAI(model = "gpt-4o", api_key = NEW_KEY)

st.title("Ask any question")

question = st.text_input("What is the question?")

if question:
    response = llm.invoke(question)
    st.write(response.content)