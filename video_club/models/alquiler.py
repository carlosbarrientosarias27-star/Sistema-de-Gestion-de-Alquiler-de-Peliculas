from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class Alquiler:
    """Entidad Alquiler.

    Atributos:
        id_alquiler: int
        id_cliente: int
        codigo_pelicula: str   # ← corregido: era int, ahora str (igual que Pelicula.codigo)
        fecha_alquiler: date
        fecha_devolucion_prevista: date
        fecha_devolucion_real: Optional[date]
    """
    id_alquiler: int
    id_cliente: int
    codigo_pelicula: str        # ← corregido
    fecha_alquiler: date
    fecha_devolucion_prevista: date
    fecha_devolucion_real: Optional[date]