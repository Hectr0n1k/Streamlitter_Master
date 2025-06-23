# Importamos la librería `requests` para hacer peticiones HTTP
import requests

# Definimos la URL del endpoint que nos devuelve los datos de un usuario en formato JSON
url = "https://reqres.in/api/users/2"

# Hacemos una petición GET a esa URL y guardamos el objeto que devuelve en la variable `response`
response = requests.get(url)

# Mostramos en consola el código de estado de la respuesta (200 significa OK)
print(f"Código de estado: {response.status_code}")

# Convertimos la respuesta JSON en un diccionario de Python
data = response.json()

# Mostramos el nombre y apellidos del usuario extraídos del diccionario
print(f"Nombre: {data['data']['first_name']} {data['data']['last_name']}")

# Mostramos el correo electrónico del usuario
print(f"Email: {data['data']['email']}")