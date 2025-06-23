import streamlit as st
import requests

st.title("API: Consulta (GET) y Envío (POST)")

# CONSULTA (GET)

st.header("Consulta de usuario (GET)")

# Paso 1: Selectbox con IDs del 1 al 30


# Paso 2: Hacer la petición GET a https://dummyjson.com/users/{id}


# Paso 3: Mostrar nombre, email e imagen del usuario


# ENVÍO (POST)

st.header("Enviar nuevo usuario (POST)")

# Paso 1: Campos de entrada para nombre y profesión


# Paso 2: Botón para enviar los datos con requests.post a https://httpbin.org/post


# Paso 3: Mostrar lo que recibió el servidor