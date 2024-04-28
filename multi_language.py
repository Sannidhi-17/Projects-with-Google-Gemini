from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from PIL import Image
import google.generativeai as genai
import os


genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-pro-vision')

def get_genai_response(input, image, prompt):
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        image_parts = [{
            "mime_type": uploaded_file.type,
            "data": bytes_data
        }]
        return image_parts
    else:
        return FileNotFoundError("NO FILE IS UPLOADED")
## INITIALIZED THE STREAMLIT APPLICATION
st.set_page_config(page_title='multilingual app')

st.header("Gemini LLM Application")
input = st.text_input("Input", key='input')
uploaded_file = st.file_uploader("choose an image.... ", type = ['jpg', 'jpeg', 'png'])
image = ''
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption = 'Uploaded Image', use_column_width = True)

submit = st.button("Tell me about image")

input_prompt = ''' You are an expert in understanding invoices. We will upload a image invoices and you have to answer
any questions based on the invoice image.'''

if submit:
    ## COLLECT IMAGE DATA
    image_data = input_image_setup(uploaded_file)
    response = get_genai_response(input_prompt, image_data, input)
    st.subheader("~The response is...")
    st.write(response)
