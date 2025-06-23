# EJERCICIO - CRUD BÁSICO CON STREAMLIT Y SQLITE

# Objetivo:
# Crear una app con Streamlit para gestionar usuarios en una base de datos SQLite ('usuarios.db').

# Tabla 'usuarios' con:
# - id (INTEGER PRIMARY KEY AUTOINCREMENT)
# - nombre (TEXT)
# - email (TEXT UNIQUE)

# La app debe tener un menú lateral con 4 opciones:
# - Ver usuarios: mostrar todos en una tabla
# - Agregar: formulario para añadir nombre y email
# - Actualizar: pedir ID y nuevo nombre, hacer UPDATE
# - Eliminar: pedir ID, hacer DELETE

# Requisitos:
# - Usar SELECT, INSERT, UPDATE y DELETE
# - Usar parámetros (?, ?) para evitar inyecciones
# - Manejar errores con try/except
# - Cerrar conexión siempre con finally

# Empieza tu código debajo: