import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect("usuarios.db")
cursor = conn.cursor()

# Ejecutar una consulta para obtener todos los registros
cursor.execute("SELECT * FROM usuarios")
resultados = cursor.fetchall() # fetchall recupera los datos de un select

# Mostrar los resultados
for registro in resultados:
    print(f"ID: {registro[0]}, Nombre: {registro[1]}, Email: {registro[2]}")

# Ejecutamos una segunda consulta
# Usamos LIKE con % para buscar coincidencias parciales
filtro_nombre = "%Ana%"  # Buscará cualquier nombre que contenga "Ana"
cursor.execute("SELECT * FROM usuarios WHERE nombre LIKE ?", (filtro_nombre,))
filtrados = cursor.fetchall()

print("\nUsuarios cuyo nombre contiene 'Ana':")
for registro in filtrados:
    print(f"ID: {registro[0]}, Nombre: {registro[1]}, Email: {registro[2]}")

# Cerrar la conexión
conn.close()