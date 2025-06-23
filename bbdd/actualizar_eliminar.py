
# Script para actualizar y eliminar usuarios con manejo de errores

import sqlite3  # Importamos sqlite

try:
    # Establecemos conexión con la base de datos
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()

    # Actualizar nombre de usuario
    # Cambiar el nombre del usuario con ID 1 a "María López"
    result_update = cursor.execute(
        "UPDATE usuarios SET nombre = ? WHERE id = ?",
        ("María López", 1)
    )

    # Verificamos si se actualizó algún registro
    if result_update.rowcount == 0:
        print("No se encontró un usuario con ese ID para actualizar.")
    else:
        print("Usuario actualizado correctamente.")

    # Eliminar usuario
    result_delete = cursor.execute(
        "DELETE FROM usuarios WHERE id = ?",
        (7,)
    )

    # Verificamos si se eliminó algún registro
    if result_delete.rowcount == 0:
        print("No se encontró un usuario con ese ID para eliminar.")
    else:
        print("Usuario eliminado correctamente.")

    # Guardamos los cambios realizados
    conn.commit()

# MANEJO DE ERRORES
except Exception as e:
    # Si algo sale mal, mostramos el error
    print(f"Error al ejecutar la operación: {e}")

# CIERRE DE CONEXIÓN
finally:
    # Nos aseguramos de cerrar la conexión aunque haya error
    if conn:
        conn.close()