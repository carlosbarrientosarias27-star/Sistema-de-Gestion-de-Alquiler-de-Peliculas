from dataclasses import dataclass

@dataclass
class Multa:
    """Entidad Multa.

    Atributos:
        id_multa: int
        id_alquiler: int
        dias_retraso: int
        importe: float
    """
    id_multa: int
    id_alquiler: int
    dias_retraso: int
    importe: float

    @staticmethod
    def calcular_importe(dias_retraso: int) -> float:
        """Calcula el importe de la multa.

        Input:
            dias_retraso: int
        Output:
            float (0.0 si dias_retraso <= 0)
        """
        raise NotImplementedError