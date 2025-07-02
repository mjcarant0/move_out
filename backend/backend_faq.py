import sqlite3
import os

# Path to database inside move_out/data/
DB_PATH = os.path.join(os.path.dirname(__file__), '../data/faq.db')

def initialize_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS faqs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insert_faq(question, answer):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO faqs (question, answer) VALUES (?, ?)", (question, answer))
    conn.commit()
    conn.close()

def search_faqs(keyword):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT question, answer FROM faqs WHERE question LIKE ?", (f"%{keyword}%",))
    results = cursor.fetchall()
    conn.close()
    return results

# Auto-initialize the database if not already created
initialize_db()
