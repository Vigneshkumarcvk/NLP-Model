import sys
import streamlit as st
sys.path.append("src")
from predict import predict_news
st.title("Fake News Detection using NLP")
st.write("Enter a news article below to check if it is Fake or Real")
news_text = st.text_area("Enter News Text", height = 200)
if st.button("Detect News"):
  if news_text.strip() == "":
    st.warning("Please enter some text")
  else:
    result = predict_news(news_text)

    if result == "Fake News":
      st.error("Fake nNews Detected")
    else:
      st.sucess("Real News")
