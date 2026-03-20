import sqlite3

class Database:
    """Gestiona la conexión SQLite y la creación de tablas."""

    def __init__(self, db_name: str = "video_club.db") -> None:
        self.db_name = db_name
        self.conn = None

    def connect(self) -> None:
        """Establece conexión con la base de datos."""
        self.conn = sqlite3.connect(self.db_name)

    def create_tables(self) -> None:
        """Crea las tablas necesarias si no existen."""
        cursor = self.conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS pelicula (
            codigo TEXT PRIMARY KEY,
            titulo TEXT,
            director TEXT,
            copias_disponibles INTEGER
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS cliente (
            id_cliente INTEGER PRIMARY KEY,
            nombre TEXT,
            email TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS alquiler (
            id_alquiler INTEGER PRIMARY KEY,
            id_cliente INTEGER,
            id_pelicula TEXT,
            fecha_alquiler TEXT,
            fecha_devolucion_prevista TEXT,
            fecha_devolucion_real TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS multa (
            id_multa INTEGER PRIMARY KEY,
            id_alquiler INTEGER,
            dias_retraso INTEGER,
            importe REAL
        )
        """)

        self.conn.commit()