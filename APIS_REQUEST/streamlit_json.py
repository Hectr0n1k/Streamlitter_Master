# Importamos las librerías necesarias
import streamlit as st
import requests

# Título principal de la aplicación
st.title("👤 Usuario desde API")

# Definimos la URL del endpoint para obtener los datos del usuario con ID 2
url = "https://dummyjson.com/users/2"

# Hacemos una petición GET a la API
response = requests.get(url)

# Verificamos que la respuesta fue correcta (código 200)
if response.status_code == 200:
    # Convertimos la respuesta en JSON directamente en un diccionario (sin clave 'data')
    user = response.json()

    # Mostramos el nombre completo del usuario
    st.write(f"**Nombre:** {user['firstName']} {user['lastName']}")

    # Mostramos el email del usuario
    st.write(f"**Email:** {user['email']}")

    # Mostramos la imagen del usuario
    st.image(user["image"])
else:
    # En caso de error, mostramos un mensaje en pantalla
    st.error("No se pudo cargar el usuario.")