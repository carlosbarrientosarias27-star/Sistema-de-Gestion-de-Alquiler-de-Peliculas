from datetime import date
from typing import List
from video_club.models.alquiler import Alquiler


class AlquilerService:
    """Servicio de gestión de alquileres."""

    def alquilar_pelicula(self, id_cliente: int, codigo: str, dias: int) -> Alquiler:
        """Crea un alquiler.

        Input:
            id_cliente: int
            codigo: str
            dias: int
        Output:
            Alquiler

        Casos límite:
            - Sin copias disponibles → ValueError
        """
        raise NotImplementedError

    def devolver_pelicula(self, id_alquiler: int, fecha_real: date) -> None:
        """Registra devolución.

        Input:
            id_alquiler: int
            fecha_real: date
        Output:
            None

        Casos límite:
            - Alquiler inexistente o ya devuelto → ValueError
        """
        raise NotImplementedError

    def listar_alquileres_activos(self) -> List[Alquiler]:
        """Lista alquileres activos.

        Output:
            list[Alquiler]
        """
        raise NotImplementedError