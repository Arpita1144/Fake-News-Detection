import streamlit as st
from backend.auth import authenticate_user

st.title("🔐 Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login", width="stretch"):

    user = authenticate_user(username, password)

    if user:
        st.success("Login Successful")
        st.session_state["user"] = username
    else:
        st.error("Invalid Username or Password")