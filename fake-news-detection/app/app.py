import sys
import os
import streamlit as st

# Add src folder to path
sys.path.append(os.path.abspath("../src"))

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
