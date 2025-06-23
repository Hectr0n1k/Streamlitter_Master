
# HOJA DE EJERCICIOS - API - PETICIONES HTTP + JSON
# Objetivo: Practicar el uso de `requests` y el manejo de respuestas JSON

# Requiere: pip install requests

import requests


# EJERCICIO 1: Obtener datos de un usuario


# Instrucción: Haz una petición GET a https://dummyjson.com/users/1
# y muestra el nombre completo (firstName + lastName)

# Escribe tu código aquí:




#  EJERCICIO 2: Mostrar el email y el teléfono

# Instrucción: A partir de la misma respuesta del ejercicio 1,
# imprime el email y el número de teléfono del usuario




# EJERCICIO 3: Mostrar datos de varios usuarios (IDs del 1 al 5)

# Instrucción: Usa un bucle para obtener los nombres de los usuarios 1 al 5




# EJERCICIO 4: Validar el código de estado HTTP

# Instrucción: Si el código de estado no es 200, muestra un mensaje de error




# EJERCICIO 5: Crear una función `get_user_name(id)` que devuelva el nombre completo

# Instrucción: Usa una función que reciba un ID y devuelva el nombre del usuario como string




# EJERCICIO 6: Mostrar los datos completos en formato JSON

# Instrucción: Usa response.json() y muestra el resultado con identación
# usando el módulo `json` de Python


# EJERCICIO 7:
# Crea un script que envíe los datos de un usuario (nombre, profesión) a una API mediante una petición POST.
# Luego imprime en consola los datos que fueron enviados al servidor, tal como los recibió.
