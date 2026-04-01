# 🎬 Sistema de Gestión de Videoclub

Sistema de gestión de alquiler de películas desarrollado en Python con arquitectura por capas (modelos, repositorios, servicios y UI).

---

# 📁 Estructura del Proyecto

```
SISTEMA-DE-GESTION-DE-ALQ.../
├── .github/
│   └── workflows/
│       └── pipeline.yml
├── tests/
│   ├── test_alquiler_service.py
│   ├── test_cliente_service.py
│   ├── test_cliente.py
│   ├── test_multa.py
│   ├── test_pelicula.py
│   └── test_videoclub.py
├── video_club/
│   ├── database/
│   │   ├── connection.py
│   │   └── init_db.py
│   ├── models/
│   │   ├── alquiler.py
│   │   ├── cliente.py
│   │   ├── multa.py
│   │   └── pelicula.py
│   ├── repositories/
│   │   ├── alquiler_repository.py
│   │   ├── cliente_repository.py
│   │   └── pelicula_repository.py
│   ├── services/
│   │   ├── alquiler_service.py
│   │   ├── cliente_service.py
│   │   ├── multa_service.py
│   │   └── pelicula_service.py
│   └── ui/
│       └── menu.py
├── conftest.py
├── main.py
├── requirements.txt
├── pytest.ini
├── .gitignore
└── README.md
```

---

# 🤖 Prompts Utilizados para Desarrollar este Proyecto

A continuación se detallan los prompts empleados con IA para generar cada parte del sistema.

---

## 1. 🏗️ Arquitectura General del Proyecto

```
Crea un sistema de gestión de videoclub en Python con arquitectura por capas:
- models: clases de dominio (Pelicula, Cliente, Alquiler, Multa)
- repositories: acceso a base de datos SQLite por entidad
- services: lógica de negocio por entidad
- ui: menú interactivo por consola
- database: conexión y inicialización de la BD
- tests: pruebas unitarias con pytest para servicios y modelos
Usa buenas prácticas: separación de responsabilidades, inyección de dependencias y nombres en español.
```

---

## 2. 🗄️ Base de Datos

```
Crea los archivos connection.py e init_db.py para una base de datos SQLite del videoclub.
- connection.py debe gestionar la conexión reutilizable.
- init_db.py debe crear las tablas: peliculas, clientes, alquileres y multas con sus relaciones.
Incluye claves foráneas y manejo de errores.
```

---

## 3. 🎥 Modelo Película

```
Crea la clase Pelicula en models/pelicula.py con los atributos:
id, titulo, director, anio, genero, disponible.
Incluye constructor, representación __str__ y validaciones básicas.
```

---

## 4. 👤 Modelo Cliente

```
Crea la clase Cliente en models/cliente.py con los atributos:
id, nombre, apellido, email, telefono, fecha_registro.
Incluye validación de email y método __str__.
```

---

## 5. 📋 Modelo Alquiler

```
Crea la clase Alquiler en models/alquiler.py con los atributos:
id, cliente_id, pelicula_id, fecha_alquiler, fecha_devolucion, devuelta.
Incluye método para calcular días de alquiler y estado de devolución.
```

---

## 6. 💰 Modelo Multa

```
Crea la clase Multa en models/multa.py con los atributos:
id, alquiler_id, monto, motivo, pagada.
Incluye método para calcular el monto según días de retraso.
```

---

## 7. 🗃️ Repositorios

```
Crea los repositorios para cada entidad (alquiler_repository.py, cliente_repository.py, pelicula_repository.py)
con los métodos CRUD: crear, obtener_por_id, obtener_todos, actualizar, eliminar.
Usa el patrón Repository con SQLite y el módulo connection.py.
```

---

## 8. ⚙️ Servicios

```
Crea los servicios de negocio para cada entidad:
- alquiler_service.py: registrar alquiler, devolver película, listar alquileres activos.
- cliente_service.py: registrar cliente, buscar por email, listar clientes.
- pelicula_service.py: agregar película, buscar por título, marcar disponibilidad.
- multa_service.py: generar multa por retraso, registrar pago.
Cada servicio recibe su repositorio por inyección de dependencias.
```

---

## 9. 🖥️ Menú de Consola (UI)

```
Crea un menú interactivo por consola en ui/menu.py para el videoclub con opciones para:
- Gestionar películas (agregar, buscar, listar)
- Gestionar clientes (registrar, buscar, listar)
- Registrar alquileres y devoluciones
- Ver multas y registrar pagos
- Salir
Usa un bucle while con input() y manejo de errores por opción inválida.
```

---

## 10. 🧪 Tests con Pytest

```
Crea tests unitarios con pytest para:
- test_pelicula.py: validar creación y atributos del modelo Pelicula.
- test_cliente.py: validar creación y formato de email del modelo Cliente.
- test_multa.py: validar cálculo de monto de multa.
- test_alquiler_service.py: mockear repositorio y probar lógica de alquiler y devolución.
- test_cliente_service.py: mockear repositorio y probar registro y búsqueda de clientes.
- test_videoclub.py: prueba de integración básica del flujo completo.
```

---

## 11. ⚙️ Configuración de CI/CD

```
Crea un workflow de GitHub Actions en .github/workflows/pipeline.yml que:
- Se ejecute en push y pull_request a main.
- Instale dependencias desde requirements.txt.
- Ejecute los tests con pytest y genere reporte de cobertura.
```

---

## 12. 📄 Archivos de Configuración

```
Crea los siguientes archivos de configuración para el proyecto:
- requirements.txt con: pytest, pytest-cov y cualquier dependencia necesaria.
- pytest.ini configurando testpaths = tests y opciones de verbose.
- .gitignore para Python incluyendo __pycache__, .pytest_cache, .vscode y *.pyc.
- conftest.py con fixtures compartidos para los tests (conexión BD en memoria, instancias de servicios).
```

---

# 🚀 Instalación y Uso

## Requisitos

- Python 3.14
- pip

# Instalación

```bash
git clone https://github.com/tu-usuario/sistema-de-gestion-videoclub.git
cd sistema-de-gestion-videoclub
pip install -r requirements.txt
```

## Ejecutar la aplicación

```bash
python main.py
```

## Ejecutar los tests

```bash
pytest
# Con reporte de cobertura
pytest --cov=video_club
```

---

## 🧰 Tecnologías Utilizadas

| Tecnología | Uso |
|---|---|
| Python 3.9+ | Lenguaje principal |
| SQLite | Base de datos local |
| Pytest | Framework de testing |
| GitHub Actions | CI/CD pipeline |

---

# 📝 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE MIT) para más información.