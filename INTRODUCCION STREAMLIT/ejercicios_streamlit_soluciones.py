
# 1. Hola mundo interactivo
import streamlit as st

# Título de la aplicación
st.title("Hola mundo")

# Entrada de texto para el nombre del usuario
nombre = st.text_input("¿Cómo te llamas?")

# Si se ha introducido un nombre, muestra un saludo
if nombre:
    st.success(f"Hola, {nombre} ")

# 2. Contador de clics
# Inicializa el contador en la sesión si no existe
if 'contador' not in st.session_state:
    st.session_state.contador = 0

# Botón para incrementar el contador
if st.button("Haz clic"):
    st.session_state.contador += 1

# Muestra cuántas veces se ha hecho clic
st.write(f"Has hecho clic {st.session_state.contador} veces")

# 3. Selector de color
# Muestra un selector de color y escribe el color seleccionado
color = st.color_picker("Elige un color", "#00f900")
st.write(f"Color seleccionado: {color}")

# 4. DataFrame y gráfico
import pandas as pd

# Crea un DataFrame con nombres y edades
data = pd.DataFrame({"Nombre": ["Ana", "Luis", "Carlos"], "Edad": [25, 30, 22]})

# Muestra la tabla y un gráfico de barras de edades
st.dataframe(data)
st.bar_chart(data.set_index("Nombre"))

# 5. Calculadora básica
# Entradas numéricas
num1 = st.number_input("Primer número", value=0.0)
num2 = st.number_input("Segundo número", value=0.0)

# Crea cuatro columnas para las operaciones
col1, col2, col3, col4 = st.columns(4)

# Cada botón ejecuta una operación
if col1.button("Sumar"):
    st.success(f"Resultado: {num1 + num2}")
if col2.button("Restar"):
    st.success(f"Resultado: {num1 - num2}")
if col3.button("Multiplicar"):
    st.success(f"Resultado: {num1 * num2}")
if col4.button("Dividir"):
    if num2 != 0:
        st.success(f"Resultado: {num1 / num2}")
    else:
        st.error("No se puede dividir por cero")

# 6. Encuesta
# Permite elegir entre tres lenguajes
opcion = st.radio("¿Qué lenguaje prefieres?", ["Python", "JavaScript", "C++"])

# Muestra el resultado seleccionado y un gráfico con un voto
st.write(f"Has seleccionado: {opcion}")
st.bar_chart(pd.DataFrame({opcion: [1]}, index=["Votos"]))

# 7. Adivina el número
import random

# Inicializa el número secreto si no está en la sesión
if 'secreto' not in st.session_state:
    st.session_state.secreto = random.randint(1, 100)

# Entrada numérica del usuario
guess = st.number_input("Adivina el número (1-100)", min_value=1, max_value=100, step=1)

# Botón para comprobar el número
if st.button("Comprobar"):
    if guess == st.session_state.secreto:
        st.success("¡Correcto!")
        st.session_state.secreto = random.randint(1, 100)  # Genera nuevo número secreto
    elif guess < st.session_state.secreto:
        st.warning("Demasiado bajo")
    else:
        st.warning("Demasiado alto")

# 8. Conversor de temperatura
# Selector de modo de conversión
modo = st.radio("Convertir:", ["Celsius a Fahrenheit", "Fahrenheit a Celsius"])

# Entrada de temperatura
temp = st.number_input("Temperatura")

# Realiza la conversión y muestra el resultado
if modo == "Celsius a Fahrenheit":
    st.write(f"{temp}°C = {(temp * 9/5) + 32}°F")
else:
    st.write(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")

# 9. Subida de imagen
# Carga una imagen desde el equipo
archivo = st.file_uploader("Sube una imagen", type=["png", "jpg", "jpeg"])

# Si se subió un archivo, muestra su nombre, tamaño e imagen
if archivo:
    st.image(archivo)
    st.write(f"Nombre: {archivo.name}")
    st.write(f"Tamaño: {archivo.size // 1024} KB")
