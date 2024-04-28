from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
os.environ['GOOGLE_API_KEY'] = 'AIzaSyDlngSnAed_mzapdR-IdMpA1puBZvdj2aw'
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

## LOAD THE GEMINI PRO MODEL AND RESPONSE
model = genai.GenerativeModel('gemini-pro')
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

## INITIALIZED THE STREAMLIT APP
st.set_page_config(page_title='Q&A Demo')
st.header("Gemini LLM Application")
st.subheader("Gemini based Question and Answer")
input = st.text_input("Input", key = 'input')
submit = st.button("Ask the question")

if submit:
    response = get_gemini_response(input)
    st.subheader("The response is.....")
    st.write(response)