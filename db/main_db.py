import sqlite3
from config import DB_NAME

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn


def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS student (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            grade TEXT
        )
    """)

    conn.commit()
    conn.close()