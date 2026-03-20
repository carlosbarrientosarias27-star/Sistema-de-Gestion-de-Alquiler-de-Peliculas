from dataclasses import dataclass

@dataclass
class Pelicula:
    """Entidad Pelicula.

    Atributos:
        titulo: str
        director: str
        codigo: str
        copias_disponibles: int
    """
    titulo: str
    director: str
    codigo: str
    copias_disponibles: int