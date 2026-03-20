from typing import Optional
from video_club.models.pelicula import Pelicula


class PeliculaService:
    """Servicio para operaciones sobre Pelicula."""

    def buscar_por_codigo(self, codigo: str) -> Optional[Pelicula]:
        """Busca una película por código.

        Input:
            codigo: str
        Output:
            Pelicula | None
        """
        raise NotImplementedError
