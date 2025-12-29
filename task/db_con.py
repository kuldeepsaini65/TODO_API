import sqlite3
from django.conf import settings

Saini_Local_DB = settings.BASE_DIR / "db.sqlite3"

def connect_db():
    return sqlite3.connect(Saini_Local_DB)

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            due_date TEXT,
            status TEXT DEFAULT 'PENDING'
        )
    """)
    conn.commit()
    conn.close()
