import streamlit as st
import requests

# Título de la aplicación
st.title("API: Consulta (GET) y Envío (POST)")

# Sección 1: Consulta con GET

# Cabecera para la sección de consulta
st.header("Consulta de usuario (GET)")

# Creamos un desplegable para seleccionar un ID del 1 al 30
user_id = st.selectbox("Selecciona un ID de usuario (1 a 30)", list(range(1, 31)))

# Construimos la URL usando el ID seleccionado
url_get = f"https://dummyjson.com/users/{user_id}"

# Hacemos la petición GET a la API
response_get = requests.get(url_get)

# Si la respuesta fue exitosa (código 200), mostramos los datos del usuario
if response_get.status_code == 200:
    user = response_get.json()  # Convertimos la respuesta en diccionario

    # Mostramos nombre, email e imagen
    st.write(f"Nombre: {user['firstName']} {user['lastName']}")
    st.write(f"Email: {user['email']}")
    st.image(user["image"], width=200)
else:
    # Si hubo un error en la respuesta, mostramos un mensaje
    st.error("Usuario no encontrado")


# Sección 2: Envío con POST

# Cabecera para la sección de envío
st.header("Enviar nuevo usuario (POST)")

# Campos de entrada de texto
nombre = st.text_input("Nombre")
profesion = st.text_input("Profesión")

# Botón para enviar los datos
if st.button("Enviar"):
    # Creamos el diccionario con los datos que se enviarán
    payload = {"nombre": nombre, "profesion": profesion}

    # Hacemos la petición POST enviando los datos como JSON
    response_post = requests.post("https://httpbin.org/post", json=payload)

    # Si la respuesta fue exitosa (código 200), mostramos lo que recibió el servidor
    if response_post.status_code == 200:
        recibido = response_post.json()["json"]  # Extraemos el contenido enviado
        st.success("Datos enviados correctamente")
        st.write("El servidor recibió:")
        st.json(recibido)
    else:
        st.error("Error al enviar los datos")