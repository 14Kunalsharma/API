from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def my_output(query) -> str:
    response = model.generate_content(query)
    return response.text

# UI DEVELOPMENT USING streamlit

st.set_page_config(page_title="SMART_BOT")
st.header("SMART BOT")

input = st.text_input("Input", key="input")
submit = st.button("ASK YOUR QUERY")

if submit:
    response = my_output(input)
    st.header("The Response is:")
    st.text_area(response)