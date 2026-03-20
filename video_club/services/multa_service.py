from video_club.models.multa import Multa
from video_club.database.connection import get_connection
 
 
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
            - dias_retraso <= 0 → devuelve 0.0 sin guardar nada
        """
        importe = Multa.calcular_importe(dias_retraso)
        if importe == 0.0:
            return 0.0
 
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO multa (id_alquiler, dias_retraso, importe) VALUES (?,?,?)",
            (id_alquiler, dias_retraso, importe)
        )
        conn.commit()
        conn.close()
 
        return importe
 