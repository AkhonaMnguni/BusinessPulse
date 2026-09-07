import sqlite3


def save_case(connection: sqlite3.Connection, data: dict) -> dict:
    cursor = connection.execute(
        "INSERT INTO cases (title, description, score, entity_type, entity_id) VALUES (?, ?, ?, ?, ?)",
        (data["title"], data["description"], data["score"], data["entity_type"], data["entity_id"]),
    )
    connection.commit()
    row = connection.execute("SELECT * FROM cases WHERE id = ?", (cursor.lastrowid,)).fetchone()
    return dict(row)
