from datetime import date, timedelta
from typing import List, Optional
from video_club.models.alquiler import Alquiler
from video_club.database.connection import get_connection
from video_club.services.pelicula_service import PeliculaService
from video_club.services.multa_service import MultaService

class AlquilerService:
    # Corrección 1: Type hint explícito para evitar quejas de mypy
    def __init__(self, multa_service: Optional[MultaService] = None):
        self._pelicula_service = PeliculaService()
        self._multa_service = multa_service or MultaService()

    def listar_alquileres_activos(self) -> List[Alquiler]:
        conn = get_connection()
        cursor = conn.cursor()
        # Corrección 2: Añadimos la columna al SELECT para ser "honestos"
        cursor.execute(
            "SELECT id_alquiler, id_cliente, codigo_pelicula, "
            "fecha_alquiler, fecha_devolucion_prevista, fecha_devolucion_real "
            "FROM alquiler WHERE fecha_devolucion_real IS NULL"
        )
        filas = cursor.fetchall()
        conn.close()

        return [
            Alquiler(
                id_alquiler=f[0],
                id_cliente=f[1],
                codigo_pelicula=f[2],
                fecha_alquiler=date.fromisoformat(f[3]),
                fecha_devolucion_prevista=date.fromisoformat(f[4]),
                # Asignación real aunque sepamos que es None por el WHERE
                fecha_devolucion_real=date.fromisoformat(f[5]) if f[5] else None 
            )
            for f in filas
        ]
    def alquilar_pelicula(self, id_cliente: int, codigo_pelicula: str, dias_prestamo: int) -> Alquiler:
        """Registra un alquiler y reduce el stock de la película."""
        hoy = date.today()
        fecha_prevista = hoy + timedelta(days=dias_prestamo)
        
        conn = get_connection()
        cursor = conn.cursor()
        
        try:
            # 1. Verificar stock y existencia
            cursor.execute("SELECT copias_disponibles FROM pelicula WHERE codigo = ?", (codigo_pelicula,))
            res = cursor.fetchone()
            if not res:
                raise ValueError("La película no existe.")
            if res[0] <= 0:
                raise ValueError("No hay copias disponibles.")

            # 2. Reducir stock
            cursor.execute(
                "UPDATE pelicula SET copias_disponibles = copias_disponibles - 1 WHERE codigo = ?",
                (codigo_pelicula,)
            )

            # 3. Crear registro de alquiler
            cursor.execute(
                """INSERT INTO alquiler (id_cliente, codigo_pelicula, fecha_alquiler, 
                                       fecha_devolucion_prevista) 
                   VALUES (?, ?, ?, ?)""",
                (id_cliente, codigo_pelicula, hoy.isoformat(), fecha_prevista.isoformat())
            )
            
            id_alquiler = cursor.lastrowid
            conn.commit()
            
            return Alquiler(id_alquiler, id_cliente, codigo_pelicula, hoy, fecha_prevista, None)
            
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()

    def devolver_pelicula(self, id_alquiler: int, fecha_real: date) -> None:
        """Registra la devolución, aumenta el stock y gestiona multas si aplica."""
        conn = get_connection()
        cursor = conn.cursor()

        try:
            # 1. Obtener datos del alquiler
            cursor.execute(
                "SELECT codigo_pelicula, fecha_devolucion_prevista, fecha_devolucion_real FROM alquiler WHERE id_alquiler = ?",
                (id_alquiler,)
            )
            fila = cursor.fetchone()

            if not fila:
                raise ValueError("Alquiler no encontrado.")
            if fila[2] is not None:
                raise ValueError("Esta película ya fue devuelta.")

            codigo_pelicula = fila[0]
            fecha_prevista = date.fromisoformat(fila[1])

            # 2. Actualizar fecha de devolución real
            cursor.execute(
                "UPDATE alquiler SET fecha_devolucion_real = ? WHERE id_alquiler = ?",
                (fecha_real.isoformat(), id_alquiler)
            )

            # 3. Aumentar stock de la película
            cursor.execute(
                "UPDATE pelicula SET copias_disponibles = copias_disponibles + 1 WHERE codigo = ?",
                (codigo_pelicula,)
            )

            # 4. Procesar multa si hay retraso
            dias_retraso = (fecha_real - fecha_prevista).days
            if dias_retraso > 0:
                importe = self._multa_service.calcular_multa(id_alquiler, dias_retraso)
                print(f"¡Atención! Retraso de {dias_retraso} días. Multa generada: {importe}€")

            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()