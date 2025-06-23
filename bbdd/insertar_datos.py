# INSERTAR USUARIOS

import sqlite3

# Creamos lista de usuario
usuarios = [
    ("Pepe", "pepe@mail.com"),
    ("Manuel", "manuel@mail.com"),
    ("Elena", "elena@mail.com"),
    ("Patricia", "patricia@mail.com")  # <- Email duplicado para probar el manejo de errores
]

try:
    # Conectamos la base de datos, si no existe la crea
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    # Ejecutamos INSERTS
    cursor.execute("INSERT INTO usuarios (nombre, email) VALUES (?, ?)", ("Ana María", "anamaria@mail.com"))
    cursor.execute("INSERT INTO usuarios (nombre, email) VALUES (?, ?)", ("Luis", "luis@mail.com"))
    cursor.execute("INSERT INTO usuarios (nombre, email) VALUES (?, ?)", ("Sofía", "sofia@mail.com"))

    # Ejecutamos múltiples INSERTS con executemany()
    cursor.executemany(
        "INSERT INTO usuarios (nombre, email) VALUES (?, ?)",
        usuarios
    )

    # Confirmamos los cambios, sin hacer commit no se guardan los cambios
    conn.commit()
    print("Usuarios insertados correctamente.")

except Exception as e:
    # Capturamos y mostramos cualquier error
    print(f" Error al insertar el usuario: {e}")

finally:
    # Cerramos la conexión de forma segura
    if conn:
        conn.close()