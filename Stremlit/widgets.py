import streamlit as st
import pandas as pd

st.write("Stremlit Text Ipnput")
name = st.text_input("Enter your name.")


age = st.slider("Select your age:", 0,100,25)
st.write(f"Your age is {age}")

options = ["Python", "JAVA", "C++", "Javascript"]

choice = st.selectbox("Choose your favorite language", options)
st.write(f"You selected {choice}")

if name:
    st.write(F"Hello {name}, How are you !")



data = {
"Name": ["John", "Jane", "Jake", "Jill"],
"Age" : [28, 24, 35, 40],
"City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
st.write(df)