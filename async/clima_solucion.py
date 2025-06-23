import streamlit as st  # Librería para crear interfaces web simples
import asyncio  # Módulo de asincronía nativo de Python
import aiohttp  # Librería para hacer peticiones HTTP asincrónicas

# Título principal de la aplicación
st.title("🌦 Consulta del clima actual (Open-Meteo)")

# Diccionario de ciudades y sus coordenadas (latitud, longitud)
ciudades = {
    "Madrid": (40.4168, -3.7038),
    "Barcelona": (41.3851, 2.1734),
    "Valencia": (39.4699, -0.3763),
    "Bilbao": (43.2630, -2.9350),
    "Sevilla": (37.3891, -5.9845)
}

# Widget para que el usuario seleccione múltiples ciudades
seleccion = st.multiselect(
    "Selecciona ciudades",
    list(ciudades.keys()),
    default=["Madrid", "Barcelona"]
)


# Función asincrónica que consulta el clima actual de una ciudad usando Open-Meteo
async def fetch_clima(session, ciudad, lat, lon):
    # Construimos la URL de la API con latitud y longitud
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"

    # Hacemos la petición HTTP asincrónica
    async with session.get(url) as response:
        # Esperamos la respuesta en formato JSON
        data = await response.json()
        # Extraemos la información del clima actual
        clima = data["current_weather"]
        # Devolvemos el nombre de la ciudad y los datos de clima
        return ciudad, clima


# Función principal asincrónica que lanza todas las peticiones en paralelo
async def get_climas(ciudades_seleccionadas):
    # Creamos una sesión HTTP reutilizable
    async with aiohttp.ClientSession() as session:
        # Creamos una tarea asincrónica por cada ciudad seleccionada
        tareas = [
            # * desempaqueta y devuelve los valores almacenados en ese tipo de dato
            fetch_clima(session, ciudad, *ciudades[ciudad])
            for ciudad in ciudades_seleccionadas
        ]
        # Con gather todas las tareas en paralelo y esperamos los resultados
        return await asyncio.gather(*tareas)


# Cuando el usuario hace clic en el botón, lanzamos la consulta
if st.button("Consultar clima"):
    # Ejecutamos la función asincrónica con asyncio.run()
    resultados = asyncio.run(get_climas(seleccion))

    # Mostramos el resultado para cada ciudad seleccionada
    for ciudad, clima in resultados:
        st.subheader(f"{ciudad}")
        st.write(f"Temperatura: {clima['temperature']}°C")
        st.write(f"Viento: {clima['windspeed']} km/h")
        st.write("---")
