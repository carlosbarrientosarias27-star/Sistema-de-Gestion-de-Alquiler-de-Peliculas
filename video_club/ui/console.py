class ConsoleUI:
    """Interfaz de usuario por consola."""

    def mostrar_menu(self) -> None:
        """Muestra el menú principal."""
        print("""
        1. Alquilar película
        2. Devolver película
        3. Buscar película
        4. Buscar cliente
        5. Listar alquileres activos
        0. Salir
        """)

    def ejecutar(self) -> None:
        """Ejecuta el bucle principal del menú."""
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                # Lógica no implementada
                pass
            elif opcion == "2":
                # Lógica no implementada
                pass
            elif opcion == "3":
                # Lógica no implementada
                pass
            elif opcion == "4":
                # Lógica no implementada
                pass
            elif opcion == "5":
                # Lógica no implementada
                pass
            elif opcion == "0":
                break
            else:
                print("Opción no válida")
