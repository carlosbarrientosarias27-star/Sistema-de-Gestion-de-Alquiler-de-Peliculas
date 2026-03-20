from video_club.models.multa import Multa


class MultaService:
    """Servicio para gestión de multas."""

    def calcular_multa(self, id_alquiler: int, dias_retraso: int) -> float:
        """Calcula y guarda multa.

        Input:
            id_alquiler: int
            dias_retraso: int
        Output:
            float

        Casos límite:
            - dias_retraso <= 0 → devuelve 0.0
        """
        raise NotImplementedError