import streamlit as st
from app import analyze_review, get_sentiment

st.title("Customer Review Sentiment Analyzer")
st.write(
    "Explore the sentiment of a customer review using keyword matching "
    "and a simple rule for 'not."
)
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

st.caption(
    "This is a rule-based learning project. It uses a small word list "
    "and may misread sarcasm or phrases such as 'not very good'. "
    "Points are word-based scores, not confidence percentages."
)