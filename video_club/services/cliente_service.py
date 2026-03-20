from typing import Optional
from video_club.models.cliente import Cliente
from video_club.database.connection import get_connection
 
 
class ClienteService:
    """Servicio para operaciones sobre Cliente."""
 
    def buscar_cliente(self, id_cliente: int) -> Optional[Cliente]:
        """Busca cliente por ID.
 
        Input:
            id_cliente: int
        Output:
            Cliente | None
        """
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id_cliente, nombre, email FROM cliente WHERE id_cliente = ?",
            (id_cliente,)
        )
        fila = cursor.fetchone()
        conn.close()
 
        if fila is None:
            return None
        return Cliente(id_cliente=fila[0], nombre=fila[1], email=fila[2])
 