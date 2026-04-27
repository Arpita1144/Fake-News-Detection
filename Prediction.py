import streamlit as st
from ml.inference import predict_news

st.title("🔎 Fake News Detection")

# Input text area
news_text = st.text_area(
    "Enter News Article",
    height=200,
    placeholder="Paste news here..."
)

# Buttons
col1, col2 = st.columns(2)

with col1:
    analyze = st.button("Analyze News", width="stretch")

with col2:
    clear = st.button("Clear", width="stretch")

# Analyze button logic
if analyze:

    if news_text.strip() == "":
        st.warning("⚠ Please enter news text")

    else:
        result, confidence = predict_news(news_text)

        if result == "Fake":
            st.error("🚨 FAKE NEWS")
        else:
            st.success("✅ REAL NEWS")

        st.write("Confidence:", round(confidence * 100, 2), "%")

# Clear button logic
if clear:
    st.experimental_rerun()
