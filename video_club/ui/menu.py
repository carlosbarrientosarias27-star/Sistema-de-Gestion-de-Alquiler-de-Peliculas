class Menu:
    """Interfaz de usuario por consola."""

    def mostrar_menu(self) -> None:
        """Muestra opciones del sistema.

        Output:
            None
        """
        print("""
        1. Alquilar película
        2. Devolver película
        3. Buscar película
        4. Buscar cliente
        5. Listar alquileres activos
        0. Salir
        """)

    def ejecutar(self) -> None:
        """Loop principal del menú.

        Output:
            None
        """
        raise NotImplementedError