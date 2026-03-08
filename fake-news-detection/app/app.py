import sys
import os
import streamlit as st

# Get project root directory
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))

# Add src folder to Python path
sys.path.append(os.path.join(project_root, "src"))

from predict import predict_news

st.title("Fake News Detection using NLP")

st.write("Enter a news article below to check if it is Fake or Real")

news_text = st.text_area("Enter News Text")

if st.button("Detect News"):

    if news_text.strip() == "":
        st.warning("Please enter some text")

    else:
        result = predict_news(news_text)

        if result == "Fake News":
            st.error("Fake News Detected")
        else:
            st.success("Real News")