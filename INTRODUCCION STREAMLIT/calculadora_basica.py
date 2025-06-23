# Importa la librería principal de Streamlit
import streamlit as st

# Título principal de la aplicación que aparecerá en la interfaz
st.title("🧮 Calculadora básica")

# -----------------------------
# ENTRADAS NUMÉRICAS DEL USUARIO
# -----------------------------

# Crea un campo de entrada para el primer número
# 'value=0.0' define el valor inicial mostrado en el campo
num1 = st.number_input("Primer número", value=0.0)

# Crea un campo de entrada para el segundo número
num2 = st.number_input("Segundo número", value=0.0)

# Línea separadora visual para mejorar el diseño
st.markdown("---")

# -----------------------------
# BOTONES PARA OPERACIONES
# -----------------------------

# Crea 4 columnas horizontales para organizar los botones
col1, col2, col3, col4 = st.columns(4)

# Variables que almacenarán el resultado y el nombre de la operación realizada
resultado = None
operacion = ""

# Dentro de cada columna, coloca un botón. Si se presiona, realiza la operación correspondiente

# Botón de suma
with col1:
    if st.button("➕ Sumar"):
        resultado = num1 + num2      # Realiza la suma
        operacion = "suma"           # Guarda el nombre de la operación

# Botón de resta
with col2:
    if st.button("➖ Restar"):
        resultado = num1 - num2
        operacion = "resta"

# Botón de multiplicación
with col3:
    if st.button("✖️ Multiplicar"):
        resultado = num1 * num2
        operacion = "multiplicación"

# Botón de división (con control de división por cero)
with col4:
    if st.button("➗ Dividir"):
        if num2 != 0:
            resultado = num1 / num2
            operacion = "división"
        else:
            st.error("No se puede dividir por cero")  # Muestra un mensaje de error si num2 es 0

# MOSTRAR RESULTADO

# Si se ha calculado un resultado, se muestra al usuario
if resultado is not None:
    st.success(f"El resultado de la {operacion} es: {resultado}")