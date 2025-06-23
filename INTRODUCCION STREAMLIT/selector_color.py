import streamlit as st

# Título de la app
st.title("Selector de color")

# Selector de color incorporado
color = st.color_picker("Elige un color", "#00f900")

# Mostrar el color seleccionado
st.write("Has elegido este color:", color)