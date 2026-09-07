import sqlite3

from business_sentinel.database.repositories import save_case


def create_case(connection: sqlite3.Connection, alert: dict) -> dict:
    return save_case(connection, alert)


def list_cases(connection: sqlite3.Connection) -> list[dict]:
    rows = connection.execute("SELECT * FROM cases ORDER BY created_at DESC, id DESC").fetchall()
    return [dict(row) for row in rows]
