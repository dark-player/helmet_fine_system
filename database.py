import sqlite3

DB_NAME = "violations.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Owners table
    c.execute("""
    CREATE TABLE IF NOT EXISTS owners (
        plate TEXT PRIMARY KEY,
        name TEXT
    )
    """)

    # Violations table
    c.execute("""
    CREATE TABLE IF NOT EXISTS violations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        plate TEXT,
        name TEXT,
        fine INTEGER,
        reason TEXT,
        time TEXT
    )
    """)

    # Insert sample data
    sample_data = [
        ("MH39AJ566", "Lalit Wagh"),
        ("MH12AB1234", "Rahul Sharma"),
        ("MH01XY9999", "Amit Patil")
    ]

    for plate, name in sample_data:
        try:
            c.execute("INSERT INTO owners VALUES (?, ?)", (plate, name))
        except:
            pass  # ignore duplicates

    conn.commit()
    conn.close()


def get_owner(plate):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("SELECT name FROM owners WHERE plate=?", (plate,))
    result = c.fetchone()

    conn.close()

    return result[0] if result else "Unknown"


def add_violation(plate, name, fine, reason):
    from datetime import datetime

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    c.execute("""
    INSERT INTO violations (plate, name, fine, reason, time)
    VALUES (?, ?, ?, ?, ?)
    """, (plate, name, fine, reason, str(datetime.now())))

    conn.commit()
    conn.close()