from dataclasses import dataclass

@dataclass
class Cliente:
    """Entidad Cliente.

    Atributos:
        id_cliente: int
        nombre: str
        email: str
    """
    id_cliente: int
    nombre: str
    email: str
