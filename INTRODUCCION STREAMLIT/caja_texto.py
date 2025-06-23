import streamlit as st

# Título de la app
st.title("Saludo personalizado")

# Entrada de texto para que el usuario escriba su nombre
nombre = st.text_input("¿Cómo te llamas?")

# Mostrar el saludo si el usuario ha escrito algo
if nombre:
    st.write(f"Hola, {nombre}. ¡Encantado de conocerte!")