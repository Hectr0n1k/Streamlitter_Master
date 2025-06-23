# CREACIÓN DE UNA BASE DE DATOS RELACIONAL
# Tabla de usuarios y tabla de roles

import sqlite3

try:
    # Conexión a la base de datos (la crea si no existe)
    conn = sqlite3.connect("empresa.db")
    cursor = conn.cursor()

    # Crear tabla de roles
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS roles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT UNIQUE
    )
    """)

    # Crear tabla de usuarios con clave foránea a roles
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        email TEXT UNIQUE,
        rol_id INTEGER,
        FOREIGN KEY (rol_id) REFERENCES roles(id)
    )
    """)

    # Insertamos usuarios
    # INSERT or IGNORE, inserta si no está el dato o IGNORA si está repetida por clave primaria (PRIMARY KEY) o UNIQUE
    cursor.executemany("INSERT OR IGNORE INTO roles (nombre) VALUES (?)", [
        ("admin",),
        ("editor",),
        ("lector",)
    ])

    usuarios = [
        ("Ana", "ana@mail.com", 1),  # admin
        ("Luis", "luis@mail.com", 2),  # editor
        ("Sofía", "sofia@mail.com", 2),  # editor
        ("Mario", "mario@mail.com", 3)  # lector
    ]

    # Insertar roles base si no existen
    cursor.executemany("INSERT OR IGNORE INTO roles (nombre) VALUES (?)", [
        ("admin",),
        ("editor",),
        ("lector",)
    ])

    conn.commit()
    print("Base de datos relacional creada correctamente.")

except Exception as e:
    print(f"vError al crear la base de datos: {e}")

finally:
    if conn:
        conn.close()