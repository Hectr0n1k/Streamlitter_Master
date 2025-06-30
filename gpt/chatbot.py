# Importamos las librerías necesarias
import streamlit as st
import openai

# Título de la aplicación
st.title("Chatbot")

# Configura tu clave de API de OpenAI
# Recomendado: usar st.secrets para ocultar la clave (añadirla en .streamlit/secrets.toml)
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Inicializamos el historial de mensajes si no existe aún en la sesión
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostramos el historial de la conversación
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):  # Rol "user" o "assistant"
        st.markdown(msg["content"])

# Campo de entrada para el mensaje del usuario
prompt = st.chat_input("Escribe tu pregunta...")

# Si el usuario escribe algo
if prompt:
    # Guardamos el mensaje del usuario en el historial
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Mostramos el mensaje del usuario en la interfaz
    with st.chat_message("user"):
        st.markdown(prompt)

    # Llamamos a la API de OpenAI con el historial de la conversación
    with st.chat_message("assistant"):
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",               # Puedes cambiar a otro modelo si quieres
            messages=st.session_state.messages  # Historial completo
        )

        # Extraemos la respuesta generada por el asistente
        assistant_msg = response.choices[0].message.content

        # Mostramos la respuesta del asistente en pantalla
        st.markdown(assistant_msg)

    # Añadimos la respuesta del asistente al historial
    st.session_state.messages.append({"role": "assistant", "content": assistant_msg})


# Mostrar botón de descarga debajo de la entrada del chat
import json  # Importamos  JSON

# Solo mostramos el botón si hay mensajes guardados en el historial
if st.session_state.get("messages"):
    st.markdown("### ")  # Espacio visual opcional para separar elementos en la interfaz

    # Creamos un botón de descarga que genera un archivo .json con el historial
    st.download_button(
        label="⬇Descargar conversación en JSON",  # Texto en el botón
        data=json.dumps(  # Convertimos la lista de mensajes a una cadena JSON
            st.session_state.messages,  # Lista de mensajes [{"role": ..., "content": ...}, ...]
            ensure_ascii=False,  # Permite caracteres especiales como acentos y ñ
            indent=2  # Añade formato legible (sangrado)
        ),
        file_name="conversacion.json",  # Nombre del archivo descargado
        mime="application/json"  # Tipo MIME para indicar que es un archivo JSON
    )
