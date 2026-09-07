# import sqlite3
# import os

# from config.settings import settings


# def _database_path() -> str:
#     prefix = "sqlite:///"
#     database_url = os.getenv("BUSINESS_SENTINEL_DATABASE_URL", settings.database_url)
#     return database_url.removeprefix(prefix) if database_url.startswith(prefix) else database_url


# def get_connection() -> sqlite3.Connection:
#     connection = sqlite3.connect(_database_path())
#     connection.row_factory = sqlite3.Row
#     connection.execute(
#         """CREATE TABLE IF NOT EXISTS cases (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             title TEXT NOT NULL,
#             description TEXT NOT NULL,
#             score INTEGER NOT NULL,
#             entity_type TEXT NOT NULL,
#             entity_id TEXT NOT NULL,
#             status TEXT NOT NULL DEFAULT 'open',
#             created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
#         )"""
#     )
#     connection.commit()
#     return connection







from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.settings import DATABASE_URL


class Database:
    """
    Provides a central SQLAlchemy database connection.

    Methods
    -------
    session()
        Creates a database session.

    engine()
        Returns the SQLAlchemy engine.
    """

    def __init__(self, database_url: str = DATABASE_URL):
        self._engine = create_engine(
            database_url,
            pool_pre_ping=True,
            future=True,
        )

        self._session_factory = sessionmaker(
            bind=self._engine,
            autoflush=False,
            autocommit=False,
        )

    def engine(self):
        return self._engine

    def session(self):
        return self._session_factory()


db = Database()