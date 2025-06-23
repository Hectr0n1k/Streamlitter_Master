import aiohttp
import asyncio

# Usaremos 'aiohttp.ClientSession()' para reutilizar conexiones HTTP de forma eficiente,
# reducir el coste de abrir/cerrar conexiones y aprovechar al máximo la asincronía.
# Es la forma recomendada en 'aiohttp' para hacer múltiples peticiones sin bloquear.


# Lista de endpoints públicos (JSONPlaceholder)
urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3"
]

# Función asincrónica que hace una petición HTTP y extrae el título
async def fetch(session, url):
    # Usamos 'async with' para abrir la conexión de manera segura y eficiente
    async with session.get(url) as response:
        data = await response.json() # Espero sin bloquear
        # Imprimimos el título del post recibido desde el endpoint
        print(f"{url} → Título: {data['title']}")

async def main():
    # Usamos una sesión HTTP reutilizable
    async with aiohttp.ClientSession() as session:
        # Creamos una lista de tareas usando un comprehesion list
        # Básicamente ejecuta un bucle y devuelve una lista
        tareas = [fetch(session, url) for url in urls]
        # Ejecutamos todas las tareas concurrentemente
        await asyncio.gather(*tareas)

# Lanza el programa
asyncio.run(main())
