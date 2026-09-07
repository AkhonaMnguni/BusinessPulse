import sqlite3
import os

from config.settings import settings


def _database_path() -> str:
    prefix = "sqlite:///"
    database_url = os.getenv("BUSINESS_SENTINEL_DATABASE_URL", settings.database_url)
    return database_url.removeprefix(prefix) if database_url.startswith(prefix) else database_url


def get_connection() -> sqlite3.Connection:
    connection = sqlite3.connect(_database_path())
    connection.row_factory = sqlite3.Row
    connection.execute(
        """CREATE TABLE IF NOT EXISTS cases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            score INTEGER NOT NULL,
            entity_type TEXT NOT NULL,
            entity_id TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'open',
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )"""
    )
    connection.commit()
    return connection
