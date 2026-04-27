import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "fake_news.db")

print("Looking at DB:", DB_PATH)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("SELECT username, password FROM users")
users = cursor.fetchall()

print("Users in database:", users)

conn.close()
