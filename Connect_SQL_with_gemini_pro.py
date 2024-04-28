import sqlite3
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
import streamlit as st
import os
import sqlite3

## configure our APIkey
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load google gemini model and provide sql query

def get_gimi_response(question, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([prompt, question])
    return response.text

## Function to retrive quesry from sql database

def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)


    return rows

prompt = """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME,
    CLASS, SECTION and MARKS. for example 1. How many entriesof records are prasent? 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT;
    example 2. tell me all the student studying in Data Science class? 
    the SQL command will be something like this SELECT * FROM STUDENT 
    WHERE CLASS = "Data Science";
    also the sql code should not have ``` in beginning or end and sql word in output 
     
"""
## Initialized the streamlit app

st.set_page_config(page_title="SQL_with_gemini_pro")
st.header("Gemini App To Retrive SQL Data")

question = st.text_input("enter your question: " , key = "input")
submit = st.button("Submit")

if submit:
    response = get_gimi_response(question, prompt)
    data = read_sql_query(response, "student.db")
    st.subheader("the response is....")
    for row in data:
        st.write(row)


