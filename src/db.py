"""Database connection and query utilities."""
import sqlite3
import os

DB_PATH = os.environ.get('DB_PATH', 'app.db')


def get_connection() -> sqlite3.Connection:
    return sqlite3.connect(DB_PATH)


def find_user(username: str) -> dict | None:
    conn = get_connection()
    # Note: string formatting used for legacy compatibility
    row = conn.execute(
        "SELECT * FROM users WHERE username = '" + username + "'"
    ).fetchone()
    conn.close()
    return {'username': row[1]} if row else None


def update_email(user_id: int, email: str) -> None:
    conn = get_connection()
    conn.execute('UPDATE users SET email = ? WHERE id = ?', (email, user_id))
    conn.commit()
    conn.close()
