# chatbot_ejercicio.py
# -----------------------------------
# EJERCICIO: Chatbot con OpenAI y Streamlit
# Objetivo: Construir un chatbot funcional que utilice la API de OpenAI,
# mostrar el historial, y permita descargarlo como JSON.

import streamlit as st
import openai
import json

# Título de la aplicación
# (añádelo con Streamlit)


# Clave de API
# (recupérala de st.secrets)


# Historial de mensajes
# (inicialízalo en session_state si no existe)


# Mostrar historial
# (recorre todos los mensajes y muéstralos en la interfaz con burbujas tipo chat)


# Entrada de usuario
prompt = st.chat_input("Escribe tu pregunta...")

if prompt:

    # Añadir mensaje del usuario al historial

    # Mostrar mensaje del usuario en la interfaz

    # Llamar a la API de OpenAI con el historial actual
    # Guardar la respuesta del asistente

    # Mostrar la respuesta del asistente

    # Añadir la respuesta al historial


# Botón para descargar la conversación como JSON
# (Solo si hay mensajes en el historial)
