# chatbot_interface.py

# Importamos Streamlit
import streamlit as st
import json

# Título de la aplicación
st.title("🧠 Chatbot con OpenAI")

# Inicializar el historial de conversación
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar historial anterior en formato chat
for mensaje in st.session_state.messages:
    with st.chat_message(mensaje["role"]):
        st.markdown(mensaje["content"])

# Campo de entrada del usuario
prompt = st.chat_input("Escribe tu mensaje...")

# Si el usuario escribe algo
if prompt:
    # Añadir el mensaje del usuario al historial
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Mostrar el mensaje del usuario en pantalla
    with st.chat_message("user"):
        st.markdown(prompt)

    # AQUÍ DEBE IR LA LLAMADA A LA API DE OPENAI
    # assistant_msg = obtener_respuesta("gpt-3.5-turbo", st.session_state.messages)

    # Aquí se muestra el mensaje del asistente (simulado por ahora)
    assistant_msg = "**[Aquí iría la respuesta del asistente]**"

    with st.chat_message("assistant"):
        st.markdown(assistant_msg)

    # Guardar la respuesta en el historial
    st.session_state.messages.append({"role": "assistant", "content": assistant_msg})

# Botón de descarga del historial
if st.session_state.messages:
    st.download_button(
        label="⬇️ Descargar conversación",
        data=json.dumps(st.session_state.messages, ensure_ascii=False, indent=2),
        file_name="conversacion.json",
        mime="application/json"
    )
