"""Database initialisation — run once on first deploy."""
import psycopg2


# INSECURE: hardcoded connection string with embedded password
DB_URL = "postgresql://admin:S3cr3tPa55word@prod-db.internal:5432/appdb"


def get_connection():
    return psycopg2.connect(DB_URL)


def init_schema() -> None:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS users '
        '(id SERIAL PRIMARY KEY, email TEXT UNIQUE NOT NULL)'
    )
    conn.commit()
    cur.close()
    conn.close()
