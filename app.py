import streamlit as st
import os

st.set_page_config(
    page_title="Fake News Detection System",
    page_icon="📰",
    layout="wide"
)

# Load CSS
css_path = os.path.join("assets", "style.css")

if os.path.exists(css_path):
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title("📰 AI Powered Fake News Detection")

st.markdown("""
Welcome to the **Fake News Detection Platform**

""")

st.image(
    "https://images.unsplash.com/photo-1504711434969-e33886168f5c",
    width=900
)