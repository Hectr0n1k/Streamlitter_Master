import sqlite3

# Ejercicio 1: Crear la base de datos y tabla 'trabajadores'
conn = sqlite3.connect("trabajadores.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS trabajadores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    email TEXT UNIQUE
)
""")
conn.commit() # Hago commit
conn.close() # Cierro conexión

# Ejercicio 2: Insertar varios trabajadores
trabajadores = [
    ("Ana", "ana@mail.com"),
    ("Luis", "luis@mail.com"),
    ("Sofía", "sofia@mail.com")
]
cursor.executemany("INSERT INTO trabajadores (nombre, email) VALUES (?, ?)", trabajadores)
conn.commit()
conn.close()

# Ejercicio 3: Consultar todos los trabajadores
cursor.execute("SELECT * FROM trabajadores")
resultados = cursor.fetchall()
for registro in resultados:
    print(f"ID: {registro[0]} - Nombre: {registro[1]} - Email: {registro[2]}")
conn.close()

# Ejercicio 4: Buscar un trabajador por nombre
nombre = input("Nombre del trabajador: ")
cursor.execute("SELECT * FROM trabajadores WHERE nombre = ?", (nombre,))
trabajador = cursor.fetchone()
if trabajador:
    print(trabajador)
else:
    print("No encontrado.")
conn.close()

# Ejercicio 5: Actualizar el nombre de un trabajador
id_trabajador = int(input("ID del trabajador: "))
nuevo_nombre = input("Nuevo nombre: ")
cursor.execute("UPDATE trabajadores SET nombre = ? WHERE id = ?", (nuevo_nombre, id_trabajador))
conn.commit()
conn.close()

# Ejercicio 6: Eliminar un trabajador por ID
id_trabajador = int(input("ID del trabajador a eliminar: "))
cursor.execute("DELETE FROM trabajadores WHERE id = ?", (id_trabajador,))
conn.commit()
conn.close()

# Ejercicio 7: Manejo de errores en inserción
try:
    cursor.execute("INSERT INTO trabajadores (nombre, email) VALUES (?, ?)", ("Ana", "ana@mail.com"))
    conn.commit()
except sqlite3.IntegrityError:
    print("El email ya existe.")
finally:
    conn.close()

# Ejercicio 8: Mostrar trabajadores con filtro en el nombre
filtro = input("Buscar por: ")
cursor.execute("SELECT * FROM trabajadores WHERE nombre LIKE ?", (f"%{filtro}%",))
resultados = cursor.fetchall()
for fila in resultados:
    print(fila)
conn.close()