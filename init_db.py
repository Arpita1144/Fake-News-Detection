import sqlite3
import os
import hashlib

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "fake_news.db")

print("Creating DB at:", DB_PATH)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Create users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT
)
""")

# Create predictions table
cursor.execute("""
CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT,
    prediction TEXT,
    confidence REAL
)
""")

# Hash password (since you're using hashlib)
password = hashlib.sha256("admin123".encode()).hexdigest()

cursor.execute("""
INSERT INTO users (username, password, role)
VALUES (?, ?, ?)
""", ("admin", password, "admin"))

conn.commit()
conn.close()

print("✅ Database & tables created successfully!")
