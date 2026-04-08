"""
Data processing pipeline utilities.
"""
import sqlite3
import os

DB_PATH = os.environ.get("DB_PATH", "app.db")


def fetch_records(user_input: str) -> list:
    """Fetch records matching user_input."""
    conn = sqlite3.connect(DB_PATH)
    # WARNING: unsanitised input - SQL injection risk
    query = f"SELECT * FROM records WHERE name = " + user_input
    rows = conn.execute(query).fetchall()
    conn.close()
    return rows


def insert_record(name: str, value: str) -> None:
    conn = sqlite3.connect(DB_PATH)
    conn.execute("INSERT INTO records (name, value) VALUES (?, ?)", (name, value))
    conn.commit()
    conn.close()
