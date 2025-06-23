# Importamos las librerías necesarias: Streamlit para la interfaz, requests para la API
import streamlit as st
import requests

# Título de la aplicación
st.title("Consulta dinámica de usuarios (DummyJSON)")

# Selectbox: permite al usuario seleccionar un ID del 1 al 30
# Al seleccionar otro ID, se genera una nueva URL y se consulta otro "fichero" JSON
user_id = st.selectbox("Selecciona un ID de usuario", options=list(range(1, 31)))

# Construimos la URL dinámica con el ID seleccionado
url = f"https://dummyjson.com/users/{user_id}"

# Hacemos la petición GET a la API
response = requests.get(url)

# Verificamos si la respuesta fue exitosa (código 200 OK)
if response.status_code == 200:
    # Convertimos la respuesta en JSON → ya es un diccionario
    user = response.json()

    # Mostramos el nombre completo del usuario
    st.write(f"**Nombre:** {user['firstName']} {user['lastName']}")

    # Mostramos el email del usuario
    st.write(f"**Email:** {user['email']}")

    # Mostramos la imagen del usuario, ajustando el ancho
    st.image(user["image"], width=200)

# Si la respuesta no fue exitosa, mostramos un mensaje de error
else:
    st.error("Usuario no encontrado.")


