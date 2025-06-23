import streamlit as st
import asyncio
import aiohttp

# Título de la aplicación
# Escribe aquí el título con st.title()


# Diccionario de ciudades con sus coordenadas (latitud, longitud)
ciudades = {
    "Madrid": (40.4168, -3.7038),
    "Barcelona": (41.3851, 2.1734),
    "Valencia": (39.4699, -0.3763)
}

# Selector de ciudades
# Crea un multiselect con st.multiselect() para elegir una o más ciudades
# Guarda el resultado en una variable llamada 'seleccion'


# Función asincrónica que consulta el clima actual de una ciudad
# Define una función async llamada fetch_clima(session, ciudad, lat, lon)
# Dentro de la función:
#   - Construye la URL con los parámetros de latitud y longitud
#     (usa la API: https://api.open-meteo.com/v1/forecast?...&current_weather=true)
url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
#   - Haz una petición HTTP asincrónica con session.get(url)
#   - Convierte la respuesta a JSON
#   - Extrae los campos de temperatura y viento
#   - Devuelve la ciudad, la temperatura y el viento


# Función principal asincrónica para lanzar todas las consultas
# Define una función async llamada get_climas(ciudades_seleccionadas)
# Dentro:
#   - Crea una sesión HTTP con async with aiohttp.ClientSession()
#   - Crea una lista de tareas usando fetch_clima() para cada ciudad
#   - Usa asyncio.gather() para ejecutar todas las tareas en paralelo
#   - Devuelve los resultados


# Lógica del botón
# Crea un botón con st.button("Consultar clima")
# Cuando se pulse:
#   - Ejecuta asyncio.run(get_climas(seleccion))
#   - Itera sobre los resultados y muestra la información:
#     ciudad, temperatura, velocidad del viento
#     usando st.subheader() y st.write()
