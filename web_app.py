import streamlit as st
from app import analyze_review, get_sentiment

st.title("Customer Review Sentiment Analyzer")

review = st.text_area("Enter a customer review:")

if st.button("Analyze"):
    if not review.strip():
        st.warning("Please enter a review.")
    else:
        positive, negative, matched = analyze_review(review)
        sentiment = get_sentiment(positive, negative)

        st.subheader(f"Sentiment: {sentiment}")
        st.write("Positive points:", positive)
        st.write("Matched words:", ", ".join(matched) if matched else "None")
      