import sys

class ConsoleUI:
    """Maneja la interacción con el usuario por terminal."""

    def __init__(self, service):
        self.service = service

    def mostrar_menu(self) -> None:
        """Imprime las opciones disponibles."""
        print("\n--- SISTEMA DE GESTIÓN VIDEO CLUB ---")
        print("1. Alquilar Película")
        print("2. Devolver Película")
        print("3. Buscar Película")
        print("4. Listar Alquileres Activos")
        print("5. Salir")

    def ejecutar(self) -> None:
        """Bucle principal de la aplicación UI."""
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self._menu_alquilar()
            elif opcion == "2":
                self._menu_devolver()
            elif opcion == "3":
                self._menu_buscar()
            elif opcion == "4":
                self._menu_listar_activos()
            elif opcion == "5":
                print("Saliendo del sistema...")
                sys.exit()
            else:
                print("Opción no válida.")

    def _menu_alquilar(self) -> None:
        """Solicita datos para alquilar."""
        pass

    def _menu_devolver(self) -> None:
        """Solicita datos para devolver."""
        pass

    def _menu_buscar(self) -> None:
        """Solicita código para buscar película."""
        pass

    def _menu_listar_activos(self) -> None:
        """Muestra los alquileres pendientes."""
        pass