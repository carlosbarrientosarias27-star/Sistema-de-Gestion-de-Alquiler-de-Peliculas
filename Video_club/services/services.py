from datetime import date
from typing import List, Optional
from Video_club.models.peliculas import Pelicula, Cliente, Alquiler, Multa
from database.database import DatabaseManager

class VideoClubService:
    """Capa de servicios para la lógica de negocio."""

    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager

    def alquilar_pelicula(self, id_cliente: int, codigo: str, dias: int) -> Alquiler:
        """
        Registra un nuevo alquiler.
        :raises ValueError: Si no hay copias disponibles o el cliente/película no existen.
        :return: Objeto Alquiler creado.
        """
        raise NotImplementedError("Lógica de decremento de copias y registro de alquiler pendiente.")

    def devolver_pelicula(self, id_alquiler: int, fecha_real: date) -> None:
        """
        Registra la devolución y gestiona la generación de multas si aplica.
        :raises ValueError: Si el alquiler no existe o ya fue devuelto.
        """
        raise NotImplementedError("Lógica de devolución y cálculo de multa.")

    def calcular_multa(self, dias_retraso: int) -> float:
        """
        Calcula el importe de la multa basado en los días.
        :return: float con el importe. 0.0 si dias_retraso <= 0.
        """
        raise NotImplementedError("Lógica de cálculo: importe = dias_retraso * tasa.")

    def buscar_por_codigo(self, codigo: str) -> Optional[Pelicula]:
        """Busca una película por su código identificador."""
        raise NotImplementedError()

    def buscar_cliente(self, id_cliente: int) -> Optional[Cliente]:
        """Busca un cliente por su ID único."""
        raise NotImplementedError()

    def listar_alquileres_activos(self) -> List[Alquiler]:
        """Retorna lista de alquileres cuya fecha_real es None."""
        raise NotImplementedError()