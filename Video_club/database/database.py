import sqlite3
from typing import Optional

class DatabaseManager:
    """Maneja la conexión y creación de tablas en SQLite."""

    def __init__(self, db_name: str = "videoclub.db"):
        self.db_name = db_name
        self._create_tables()

    def _create_tables(self) -> None:
        """Crea las 4 tablas principales si no existen."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            # Tablas: Pelicula, Cliente, Alquiler, Multa
            cursor.executescript("""
                CREATE TABLE IF NOT EXISTS peliculas (
                    codigo TEXT PRIMARY KEY,
                    titulo TEXT NOT NULL,
                    director TEXT NOT NULL,
                    copias_disponibles INTEGER DEFAULT 0
                );
                CREATE TABLE IF NOT EXISTS clientes (
                    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    email TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS alquileres (
                    id_alquiler INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_cliente INTEGER,
                    id_pelicula TEXT,
                    fecha_alquiler DATE,
                    fecha_prevista DATE,
                    fecha_real DATE,
                    FOREIGN KEY(id_cliente) REFERENCES clientes(id_cliente),
                    FOREIGN KEY(id_pelicula) REFERENCES peliculas(codigo)
                );
                CREATE TABLE IF NOT EXISTS multas (
                    id_multa INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_alquiler INTEGER,
                    dias_retraso INTEGER,
                    importe REAL,
                    FOREIGN KEY(id_alquiler) REFERENCES alquileres(id_alquiler)
                );
            """)
            conn.commit()

    def get_connection(self):
        """Retorna una conexión activa a la base de datos."""
        return sqlite3.connect(self.db_name)