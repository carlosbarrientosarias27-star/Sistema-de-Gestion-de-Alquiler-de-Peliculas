from typing import Optional
from video_club.models.cliente import Cliente


class ClienteService:
    """Servicio para operaciones sobre Cliente."""

    def buscar_cliente(self, id_cliente: int) -> Optional[Cliente]:
        """Busca cliente por ID.

        Input:
            id_cliente: int
        Output:
            Cliente | None
        """
        raise NotImplementedError