# CRUD (CREATE, READ, UPDATE, DELETE) de usuarios con Streamlit y SQLite
import streamlit as st          # Importamos streamlit
import sqlite3                 # Para la conexión con SQLite
import pandas as pd            # Para manipular y mostrar datos como tablas

# Función reutilizable para obtener la conexión a la base de datos
def get_connection():
    return sqlite3.connect("usuarios.db")

# Título principal de la app
st.title("Gestión de Usuarios")

# Menú lateral izquierdo con opciones del CRUD
menu = st.sidebar.selectbox("Opciones", ["Ver usuarios", "Agregar", "Actualizar", "Eliminar"])

# Opción 1 - ver usuarios
if menu == "Ver usuarios":
    conn = None  # Declaración previa
    try:
        conn = get_connection()  # Conectamos a la base de datos
        df = pd.read_sql_query("SELECT * FROM usuarios", conn)  # Ejecutamos SELECT y lo cargamos en DataFrame
        st.dataframe(df)  # Mostramos la tabla
    except Exception as e:
        st.error(f"Error al consultar la base de datos: {e}")  # Mostramos el error en la interfaz
    finally:
        if conn:
            conn.close()

# Opción 2: Agregar nuevo usuario
elif menu == "Agregar":
    nombre = st.text_input("Nombre")  # Campo para nombre
    email = st.text_input("Email")    # Campo para email

    if st.button("Agregar"):  # Si se presiona el botón
        if nombre and email:  # Validamos que no estén vacíos
            conn = None  # Declaración previa
            try:
                conn = get_connection()
                conn.execute("INSERT INTO usuarios (nombre, email) VALUES (?, ?)", (nombre, email))  # Inserta los datos
                conn.commit()  # Guarda los cambios
                st.success("Usuario agregado")  # Mensaje de éxito
            except Exception as e:
                st.error(f"No se pudo agregar el usuario: {e}")  # Captura y muestra error
            finally:
                if conn:
                    conn.close()
        else:
            st.warning("Por favor, completa todos los campos.")  # Validación simple

# Opción 3: Actualizar nombre del usuario
elif menu == "Actualizar":
    id_usuario = st.number_input("ID del usuario", min_value=1)  # Campo para el ID
    nuevo_nombre = st.text_input("Nuevo nombre")  # Campo para el nuevo nombre

    if st.button("Actualizar"):
        conn = None  # Declaración previa
        if nuevo_nombre:  # Verificamos que no esté vacío
            try:
                conn = get_connection()
                result = conn.execute("UPDATE usuarios SET nombre = ? WHERE id = ?", (nuevo_nombre, id_usuario))  # Ejecuta el UPDATE
                conn.commit()

                if result.rowcount == 0:
                    st.warning("No se encontró un usuario con ese ID.")  # Si no se actualizó nada
                else:
                    st.success("Usuario actualizado")  # Confirmación
            except Exception as e:
                st.error(f"No se pudo actualizar el usuario: {e}")  # Error al actualizar
            finally:
                if conn:
                    conn.close()
        else:
            st.warning("El nuevo nombre no puede estar vacío.")  # Validación

# Opción 4: Eliminar usuario por ID
elif menu == "Eliminar":
    id_borrar = st.number_input("ID del usuario a eliminar", min_value=1)  # Campo para ID

    if st.button("Eliminar"):
        conn = None  # Declaración previa
        try:
            conn = get_connection()
            result = conn.execute("DELETE FROM usuarios WHERE id = ?", (id_borrar,))  # Ejecuta el DELETE
            conn.commit()

            if result.rowcount == 0:
                st.warning("No se encontró un usuario con ese ID.")  # No se borró nadie
            else:
                st.warning("Usuario eliminado")  # Confirmación de borrado
        except Exception as e:
            st.error(f"No se pudo eliminar el usuario: {e}")  # Captura y muestra el error
        finally:
            if conn:
                conn.close()