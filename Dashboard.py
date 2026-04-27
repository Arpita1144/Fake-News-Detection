import streamlit as st
import plotly.express as px
import pandas as pd

st.title("📊 Dashboard Overview")

# Fake data example
data = {
    "Fake": 320,
    "Real": 680
}

col1, col2, col3 = st.columns(3)

col1.metric("Total Articles", "1000")
col2.metric("Fake News Detected", "320")
col3.metric("Model Accuracy", "92%")

st.markdown("### 📈 Distribution")

df = pd.DataFrame({
    "Category": ["Fake", "Real"],
    "Count": [320, 680]
})

fig = px.pie(df, names="Category", values="Count", hole=0.6)
st.plotly_chart(fig, use_container_width=True)
