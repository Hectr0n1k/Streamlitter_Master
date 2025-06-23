# Importamos las librerías necesarias
import streamlit as st                      # Para crear la interfaz web
from openai import AsyncOpenAI              # Cliente asincrónico de la API de OpenAI
import asyncio                              # Para usar funciones async/await
import json                                 # Para convertir el historial a JSON

# Inicializamos el cliente de OpenAI con la clave leída desde secrets.toml
client = AsyncOpenAI(api_key=st.secrets["OPENAI_API_KEY"])


# ------------------------- FUNCIONES -------------------------

# Función asincrónica que llama a la API de OpenAI
# y devuelve la respuesta generada por el modelo
async def obtener_respuesta(modelo: str, mensajes: list) -> str:
    respuesta = await client.chat.completions.create(
        model=modelo,                      # Modelo a usar (ejemplo, gpt-3.5-turbo)
        messages=mensajes                  # Historial de mensajes como contexto
    )
    return respuesta.choices[0].message.content  # Extraemos solo el texto de la respuesta


# Función para mostrar todos los mensajes guardados en la sesión
def mostrar_historial():
    for mensaje in st.session_state.messages:
        # Mostramos cada mensaje por pantalla (user o assistant)
        with st.chat_message(mensaje["role"]):
            st.markdown(mensaje["content"])


# Función que permite descargar el historial completo como un archivo .json
def descargar_conversacion():
    # Solo mostramos el botón si ya hay mensajes guardados
    if st.session_state.get("messages"):
        # Convertimos la lista de mensajes a formato JSON y la ofrecemos para descarga
        st.download_button(
            label="⬇️ Descargar conversación en JSON",        # Texto del botón
            data=json.dumps(
                st.session_state.messages,                   # Lista de mensajes
                ensure_ascii=False,                          # Soporta tildes y ñ
                indent=2                                     # JSON legible con sangrado
            ),
            file_name="conversacion.json",                   # Nombre del archivo
            mime="application/json"                          # Tipo MIME
        )


# ------------------------- APLICACIÓN PRINCIPAL -------------------------

# Mostramos el título de la aplicación
st.title("Chatbot Asincrónico")

# Si no hay historial aún, lo inicializamos como lista vacía
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostramos el historial completo antes de la nueva entrada
mostrar_historial()

# Mostramos el campo de entrada para que el usuario escriba su mensaje
prompt = st.chat_input("Escribe tu pregunta...")

# Si el usuario ha enviado un mensaje
if prompt:
    # Guardamos el mensaje del usuario en el historial
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Mostramos el mensaje del usuario en la interfaz
    with st.chat_message("user"):
        st.markdown(prompt)

    # Mostramos burbuja del asistente y llamamos a la API asincrónicamente
    with st.chat_message("assistant"):
        # Ejecutamos la función asincrónica para obtener la respuesta
        assistant_msg = asyncio.run(
            obtener_respuesta("gpt-3.5-turbo", st.session_state.messages)
        )
        # Mostramos la respuesta recibida
        st.markdown(assistant_msg)

    # Guardamos la respuesta del asistente en el historial
    st.session_state.messages.append({"role": "assistant", "content": assistant_msg})

# Mostramos el botón de descarga del historial al final de la interfaz
descargar_conversacion()

