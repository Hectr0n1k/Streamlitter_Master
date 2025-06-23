# EJERCICIOS DE ASINCRONÍA EN PYTHON (VARIANTE)


import asyncio
import aiohttp

# EJERCICIO 1: Define una función asincrónica llamada iniciar_sesion()
# que imprima "Inicio", espere 1.5 segundos y luego imprima "Sesión iniciada".


# EJERCICIO 2: Simula tres tareas llamadas tarea_lenta, tarea_media y tarea_rapida
# Usa asyncio.gather() para ejecutarlas simultáneamente y haz que duren 3, 2 y 1 segundos respectivamente.


# EJERCICIO 3: Implementa una función llamada obtener_dato(session, url)
# que haga una petición HTTP a https://jsonplaceholder.typicode.com/users/1
# y muestre el nombre del usuario (campo "name").


# EJERCICIO 4: Crea una función que reciba varias URLs de usuarios (del 1 al 3)
# y obtenga todos los nombres de los usuarios en paralelo usando aiohttp y gather.


# EJERCICIO 5: Simula una operación larga (por ejemplo, con sleep de 4 segundos)
# y usa asyncio.wait_for() con un timeout de 2 segundos. Captura y muestra el TimeoutError.


# EJERCICIO 6: Lanza una tarea asincrónica que dure 5 segundos y cancélala manualmente después de 1 segundo.
# Imprime "tarea cancelada" si se cancela correctamente.


# EJERCICIO 7: Escribe una función que devuelva ('Sevilla', 26.7) como tupla
# Luego cambia para devolver ['Sevilla', 26.7] como lista
# Finalmente haz que devuelva {'ciudad': 'Sevilla', 'temp': 26.7}

