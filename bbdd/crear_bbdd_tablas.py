import sqlite3

try:
    # Conectar a la base de datos (crea el archivo si no existe)
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    # Crear tabla si no existe, uso únique en TEXT como restricción para que no se repita el email
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        email TEXT UNIQUE 
    )
    ''')

    # Confirmar los cambios
    conn.commit()
    print("Base de datos y tabla creadas correctamente.")

except Exception as e:
    print(f" Error al crear la base de datos o la tabla: {e}")

finally:
    # Si conn es true entonces cierra
    if conn:
        conn.close()