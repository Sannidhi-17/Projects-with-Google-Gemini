from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


def gemini_model_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("no file is uploaded")


## INITIALIZED THE STREAMLIT APP

st.set_page_config(page_title = "Health Management App")
st.header("Health management App")
input = st.text_input("Input Prompt: ", key='input prompt')
uploaded_file = st.file_uploader("Choose an image...", type = ['jpeg', 'jpg', 'png'])
image = ''

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption = "uploaded Image", use_column_width = True)


submit = st.button("Submit")

input_prompt = """
You are an expert in nutritionist where you need to see the food items from the image
               and calculate the total calories, also provide the details of every food items with calories intake
               is below format

               1. Item 1 - no of calories
               2. Item 2 - no of calories
               ----
               ----

"""

if submit:
    image_data = input_image_setup(uploaded_file)
    response = gemini_model_response(input_prompt, image_data, input)
    st.subheader("the response is....")
    st.write(response)