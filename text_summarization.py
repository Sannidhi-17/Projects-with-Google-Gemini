import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
import os
from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

prompt="""You are Yotube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 250 words. Please provide the summary of the text given here:  """


def generate_gemini_content(trancript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + trancript_text)
    return response.text

## GET THE TRANSCRIPT OF YOUTUBE VIDEO

def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]

        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i['text']

        return transcript
    except Exception as e:
        raise e

## INITIALIZED STREAMLIT APP

st.title("youtube video transcript")
youtube_link = st.text_input("Enter the youtube link: ")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg")

if st.button("submit"):
    transcript_text = extract_transcript_details(youtube_link)

    if transcript_text:
        summary = generate_gemini_content(transcript_text, prompt)
        st.write(summary)