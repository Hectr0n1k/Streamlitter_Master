
# Importamos la librería principal de Streamlit
import streamlit as st

# Configura los parámetros generales de la aplicación:
# Título de la pestaña en el navegador
# Icono de la app (puede ser un emoji o ruta a una imagen)
# Diseño de la app: "centered" (centrado) o "wide" (ancho)
st.set_page_config(page_title="Demo App", page_icon="📊", layout="centered")

# Título principal que se muestra en la aplicación
st.title("Streamlit")

# Texto introductorio que aparece debajo del título
st.write("¡Bienvenido a tu app en GitHub!")

# --- SECCIÓN DE INTERACCIÓN CON EL USUARIO ---

# Entrada de texto: el usuario puede escribir su nombre
nombre = st.text_input("¿Cómo te llamas?", "")

# Slider para que el usuario seleccione su edad entre 0 y 100 (valor inicial 25)
edad = st.slider("¿Qué edad tienes?", 0, 100, 25)

# Si el usuario ha escrito su nombre, mostramos un mensaje personalizado
if nombre:
    st.success(f"Hola, {nombre}. Tienes {edad} años.")

# --- SECCIÓN DE VISUALIZACIÓN DE DATOS ---

# Importamos pandas y numpy para crear datos de ejemplo
import pandas as pd
import numpy as np

# Creamos un DataFrame con dos columnas: x (1 al 10) y y (valores aleatorios)
data = pd.DataFrame({
    'x': np.arange(1, 11),                      # Valores del 1 al 10
    'y': np.random.randint(1, 100, 10)          # 10 valores aleatorios entre 1 y 100
})

# Mostramos un gráfico de líneas con los datos creados, usando 'x' como índice
st.line_chart(data.set_index('x'))