from openai import OpenAI

# Inicializa el cliente con tu API key
client = OpenAI(api_key="TU_API_KEY_AQUÍ")

# Enviamos un único mensaje del usuario, si fuera al sistema sería system
messages = [{"role": "user", "content": "¿Qué es la inteligencia artificial?"}]

# Llamamos al modelo
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages
)

# Mostramos la respuesta
print("Asistente:", response.choices[0].message.content)


