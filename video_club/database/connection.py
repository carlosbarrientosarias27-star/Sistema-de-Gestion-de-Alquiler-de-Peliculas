import sqlite3

DB_NAME = "video_club.db"


def get_connection() -> sqlite3.Connection:
    """Devuelve conexión SQLite.

    Output:
        sqlite3.Connection
    """
    return sqlite3.connect(DB_NAME)