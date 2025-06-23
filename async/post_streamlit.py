import streamlit as st
import asyncio
import aiohttp

st.title("📥 Consulta de Posts (JSONPlaceholder)")

# Selección de número de posts a consultar
num_posts = st.slider("¿Cuántos posts quieres consultar?", min_value=1, max_value=10, value=3)

# Lista dinámica de URLs
urls = [f"https://jsonplaceholder.typicode.com/posts/{i}" for i in range(1, num_posts + 1)]


# Función asincrónica para hacer la petición a cada post
async def fetch_post(session, url):
    async with session.get(url) as response:
        return await response.json()


# Función principal asincrónica que hace todas las peticiones
async def get_all_posts(urls):
    async with aiohttp.ClientSession() as session:
        tareas = [fetch_post(session, url) for url in urls]
        return await asyncio.gather(*tareas)


# Botón para lanzar la consulta
if st.button("Consultar posts"):
    posts = asyncio.run(get_all_posts(urls))

    # Mostrar resultados
    for post in posts:
        st.subheader(post["title"])
        st.write(post["body"])
