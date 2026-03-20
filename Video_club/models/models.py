from dataclasses import dataclass
from datetime import date
from typing import Optional

@dataclass
class Pelicula:
    """Representa una película en el catálogo."""
    titulo: str
    director: str
    codigo: str
    copias_disponibles: int

@dataclass
class Cliente:
    """Representa a un socio del video club."""
    id_cliente: int
    nombre: str
    email: str

@dataclass
class Alquiler:
    """Registro de una transacción de alquiler."""
    id_alquiler: int
    id_cliente: int
    id_pelicula: int
    fecha_alquiler: date
    fecha_devolucion_prevista: date
    fecha_devolucion_real: Optional[date] = None

@dataclass
class Multa:
    """Registro de sanciones por retraso."""
    id_multa: int
    id_alquiler: int
    dias_retraso: int
    importe: float