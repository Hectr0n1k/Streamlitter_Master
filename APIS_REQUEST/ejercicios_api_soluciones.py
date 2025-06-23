# SOLUCIONES - PETICIONES HTTP + JSON

import requests
import json

# EJERCICIO 1: Obtener datos de un usuario
response = requests.get("https://dummyjson.com/users/1")
user = response.json()
print("Nombre completo:", f"{user['firstName']} {user['lastName']}")



# EJERCICIO 2: Mostrar el email y el teléfono
print("Email:", user["email"])
print("Teléfono:", user["phone"])



# EJERCICIO 3: Mostrar datos de varios usuarios (IDs del 1 al 5)
print("\nUsuarios del 1 al 5:")
for i in range(1, 6):
    r = requests.get(f"https://dummyjson.com/users/{i}")
    u = r.json()
    print(f"- {u['firstName']} {u['lastName']}")


# EJERCICIO 4: Validar el código de estado HTTP
print("\nValidando código de estado:")
url = "https://dummyjson.com/users/999"  # ID inválido para forzar error
response = requests.get(url)
if response.status_code == 200:
    print("Usuario encontrado.")
else:
    print(f"Error: código de estado {response.status_code}")


# EJERCICIO 5: Crear una función `get_user_name(id)`
def get_user_name(user_id):
    res = requests.get(f"https://dummyjson.com/users/{user_id}")
    if res.status_code == 200:
        u = res.json()
        return f"{u['firstName']} {u['lastName']}"
    else:
        return "Usuario no encontrado."

print("\nNombre del usuario con ID 3:", get_user_name(3))


# EJERCICIO 6: Mostrar los datos completos en formato JSON
print("\nDatos completos del usuario 1 (formato bonito):")
print(json.dumps(user, indent=2))



# EJERCICIO 7:
# Crea un script que envíe los datos de un usuario (nombre, profesión) a una API mediante una petición POST.
# Luego imprime en consola los datos que fueron enviados al servidor, tal como los recibió.
import requests

url = "https://httpbin.org/post"
post = {"nombre": "Ana", "profesion": "Ingeniera"}

r = requests.post(url, json=post)

if r.status_code == 200:
    print("Enviado:", r.json()["json"])
else:
    print("Error")