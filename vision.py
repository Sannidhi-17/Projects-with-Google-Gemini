from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

os.environ['GOOGLE_API_KEY'] = 'AIzaSyDlngSnAed_mzapdR-IdMpA1puBZvdj2aw'
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

## LOAD THE GEMINI PRO VISION KODEL AND RESPONSE
model_1 = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_model_response_1(input, image):
    if input != '':
        response = model_1.generate_content([input,image])
    else:
        response = model_1.generate_content(image)
    return response.text


## INITIALIZED STREMLIT APP
st.set_page_config("Image description demo")
st.header("Gemini based image demo")

input = st.text_input("Input", key = 'input')

uploaded_file = st.file_uploader("choose an image.... ", type = ['jpg', 'jpeg', 'png'])
image = ''
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption = 'Uploaded Image', use_column_width = True)

submit = st.button("Tell me about image")

if submit:
 response = get_gemini_model_response_1(input, image)
 st.subheader("The response is.....")
 st.write(response)