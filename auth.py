import hashlib
import os
from streamlit import user
import sqlite3

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "fake_news.db")


def authenticate_user(username, password):

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT username, password FROM users WHERE username=?", (username,))
    user = cursor.fetchone()

    conn.close()

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    if user and user[1] == hashed_password:
        return user

    return None
