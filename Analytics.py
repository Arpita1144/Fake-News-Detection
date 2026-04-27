import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 News Analytics")

df_fake = pd.read_csv("data/Fake.csv")
df_true = pd.read_csv("data/True.csv")

df_fake["label"] = "Fake"
df_true["label"] = "Real"

df = pd.concat([df_fake, df_true])

fig = px.pie(
    df,
    names="label",
    title="Fake vs Real News Distribution"
)

st.plotly_chart(fig, width="stretch")

df["word_count"] = df["text"].apply(lambda x: len(str(x).split()))

fig2 = px.histogram(
    df,
    x="word_count",
    nbins=40,
    title="Article Length Distribution"
)

st.plotly_chart(fig2, width="stretch")