from dataclasses import dataclass

TARIFA_DIARIA = 1.50

@dataclass
class Multa:
    id_multa: int
    id_alquiler: int
    dias_retraso: int
    importe: float

    @staticmethod
    def calcular_importe(dias_retraso: int) -> float:
        """
        Calcula el coste basado en días de retraso.
        
        Input: dias_retraso (int)
        Output: float (Importe total)
        """
        if dias_retraso <= 0:
            return 0.0
        return round(dias_retraso * TARIFA_DIARIA, 2)

    def __repr__(self) -> str:
        return f"Multa #{self.id_multa} | Alquiler #{self.id_alquiler} | {self.dias_retraso} días | {self.importe:.2f}€"