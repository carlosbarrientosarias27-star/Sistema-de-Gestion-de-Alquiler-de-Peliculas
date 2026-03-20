from typing import Optional
from video_club.models.pelicula import Pelicula
from video_club.database.connection import get_connection
 
 
class PeliculaService:
    """Servicio para operaciones sobre Pelicula."""
 
    def buscar_por_codigo(self, codigo: str) -> Optional[Pelicula]:
        """Busca una película por código.
 
        Input:
            codigo: str
        Output:
            Pelicula | None
        """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT codigo, titulo, director, copias_disponibles "
            "FROM pelicula WHERE codigo = ?",
            (codigo,)
        )
        fila = cursor.fetchone()
        conn.close()
 
        if fila is None:
            return None
        return Pelicula(
            codigo=fila[0],
            titulo=fila[1],
            director=fila[2],
            copias_disponibles=fila[3],
        )
    