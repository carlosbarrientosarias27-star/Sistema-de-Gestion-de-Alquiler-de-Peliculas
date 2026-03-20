from datetime import date
from typing import List, Optional

from video_club.models.pelicula import Pelicula
from video_club.models.cliente import Cliente
from video_club.models.alquiler import Alquiler

class VideoClubService:
    """Contiene la lógica de negocio del sistema."""

    def alquilar_pelicula(self, id_cliente: int, codigo: str, dias: int) -> Alquiler:
        """
        Realiza el alquiler de una película.
        Input: id_cliente (int), codigo (str), dias (int)
        Output: Alquiler | ValueError si no hay copias disponibles
        """
        raise NotImplementedError

    def devolver_pelicula(self, id_alquiler: int, fecha_real: date) -> None:
        """
        Procesa la devolución de una película.
        Input: id_alquiler (int), fecha_real (date)
        Output: None | ValueError si no existe o ya fue devuelto
        """
        raise NotImplementedError

    def calcular_multa(self, dias_retraso: int) -> float:
        """
        Calcula la multa en base a días de retraso.
        Input: dias_retraso (int)
        Output: float | 0.0 si dias_retraso <= 0
        """
        raise NotImplementedError

    def buscar_por_codigo(self, codigo: str) -> Optional[Pelicula]:
        """
        Busca una película por su código.
        Input: codigo (str)
        Output: Pelicula | None si no existe
        """
        raise NotImplementedError

    def buscar_cliente(self, id_cliente: int) -> Optional[Cliente]:
        """
        Busca un cliente por su ID.
        Input: id_cliente (int)
        Output: Cliente | None si no existe
        """
        raise NotImplementedError

    def listar_alquileres_activos(self) -> List[Alquiler]:
        """
        Lista los alquileres activos.
        Input: None
        Output: list[Alquiler]
        """
        raise NotImplementedError