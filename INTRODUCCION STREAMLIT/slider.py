import streamlit as st

# Título de la app
st.title("🎚️ Demo de Slider en Streamlit")

# Slider para seleccionar un número del 1 al 100
valor = st.slider(
    label="Selecciona un valor",
    min_value=1,
    max_value=100,
    value=50,         # Valor inicial
    step=1            # Incremento
)

# Muestra el valor seleccionado
st.write(f"Has seleccionado: {valor}")