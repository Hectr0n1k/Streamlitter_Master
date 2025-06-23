# Ejercicio 1: Primer mensaje al modelo
# Hacemos una petición simple a la API de OpenAI con un solo mensaje.

from openai import OpenAI

# Inicializamos el cliente con nuestra clave (sustituir con st.secrets si usas Streamlit)
client = OpenAI(api_key="TU_CLAVE_AQUI")

# Creamos una conversación con un único mensaje del usuario
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "¿Qué es la inteligencia artificial?"}]
)

# Mostramos la respuesta generada por el modelo
print(response.choices[0].message.content)


# Ejercicio 2: Usar el rol "system" para controlar el estilo
# Añadimos un mensaje inicial del sistema para modificar el comportamiento del asistente

messages = [
    {"role": "system", "content": "Responde siempre como si fueras un ingeniero."},
    {"role": "user", "content": "¿Qué es una red neuronal?"}
]

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages
)

print(response.choices[0].message.content)


# Ejercicio 3: Haz el que el chatbot funcione siempre como un traductor
# Simulamos una conversación más larga añadiendo varios mensajes

messages = [
    {"role": "system", "content": "A partir de ahora eres un traductor de inglés al español. Traduce todo los mensajes que recibas."},
    {"role": "user", "content": "Qué día tan bonito hace hoy"}
]

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=historial
)

print(response.choices[0].message.content)


# Ejercicio 4: Convertir en función reutilizable
# Creamos una función para enviar preguntas al modelo fácilmente

def consultar_gpt(prompt):
    mensajes = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=mensajes
    )
    return response.choices[0].message.content

# Prueba la función
respuesta = consultar_gpt("¿Quién escribió Don Quijote?")
print(respuesta)


# Ejercicio 5: Chat en consola con historial
# Creamos un bucle de conversación con historial acumulado

historial = [
    {"role": "system", "content": "Responde de forma sencilla y clara."}
]

while True:
    pregunta = input("Tú: ")
    if pregunta.lower() in ["salir", "exit"]:
        break

    historial.append({"role": "user", "content": pregunta})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=historial
    )

    respuesta = response.choices[0].message.content
    print("GPT:", respuesta)

    historial.append({"role": "assistant", "content": respuesta})
