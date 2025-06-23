import requests

# URL del endpoint de prueba para POST
url = "https://httpbin.org/post"

# Datos simulados que queremos enviar
payload = {
    "name": "Ramón López",
    "job": "Científico de datos"
}

# Hacemos la petición POST
response = requests.post(url, json=payload)

# Comprobamos si la respuesta fue exitosa
if response.status_code == 200:
    data = response.json()
    print("Datos enviados correctamente:")
    print("Respuesta completa:")
    print(data)  # Esto incluye lo que se envió, las cabeceras, etc.
else:
    print(" Error al enviar los datos")