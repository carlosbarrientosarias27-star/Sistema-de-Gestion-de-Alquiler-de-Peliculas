import sys
import os

# Add the current directory to the path so Python can find 'database'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from video_club.database.init_db import init_db
from video_club.ui.menu import Menu

def main() -> None:
    """Punto de entrada de la aplicación.

    Output:
        None
    """
    init_db()
    menu = Menu()
    menu.ejecutar()


if __name__ == "__main__":
    main()