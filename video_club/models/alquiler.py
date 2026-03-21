from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class Alquiler:
    id_alquiler: int
    id_cliente: int
    codigo_pelicula: str 
    fecha_alquiler: date
    fecha_devolucion_prevista: date
    fecha_devolucion_real: Optional[date]