from database.database import DatabaseManager
from services.services import VideoClubService
from ui.ui import ConsoleUI

def main():
    """Inicializa componentes y arranca la interfaz."""
    # 1. Inicializar DB (crea tablas si no existen)
    db_manager = DatabaseManager("videoclub_v1.db")
    
    # 2. Inyectar DB en el servicio
    service = VideoClubService(db_manager)
    
    # 3. Inyectar servicio en la UI
    app = ConsoleUI(service)
    
    # 4. Correr
    app.ejecutar()

if __name__ == "__main__":
    main()