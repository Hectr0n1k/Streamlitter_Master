# Importamos la librería requests, que permite hacer peticiones HTTP
import requests

# Definimos la URL del endpoint que nos devolverá los datos del usuario con ID 2
url = "https://dummyjson.com/users/2"

# Hacemos una petición GET a la URL y guardamos la respuesta en la variable `response`
response = requests.get(url)

# Verificamos si el código de estado es 200 (OK), lo que indica que la respuesta fue correcta
if response.status_code == 200:
    # Convertimos la respuesta en formato JSON a un diccionario de Python
    user = response.json()

    # Imprimimos el nombre completo del usuario
    print("Nombre completo:", f"{user['firstName']} {user['lastName']}")

    # Imprimimos el correo electrónico del usuario
    print("Email:", user["email"])

    # Imprimimos la URL de la imagen del usuario
    print("Avatar:", user["image"])
else:
    # Si el código de estado no es 200, mostramos un mensaje de error
    print("Error al obtener datos")