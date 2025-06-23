import streamlit as st  # Importamos la librería principal de Streamlit

# Configura la apariencia de la página (título del navegador y disposición del contenido)
st.set_page_config(page_title="Calculadora", layout="centered")

# Selector para elegir el color de fondo desde un menú desplegable
color_nombre = st.selectbox("Color de fondo", ["Azul claro", "Rosa claro", "Gris claro"])

# Diccionario que mapea nombres de color a sus códigos hexadecimales
colores = {
    "Azul claro": "#e0f7fa",
    "Rosa claro": "#fde2e4",
    "Gris claro": "#f0f0f0"
}

# Se selecciona el código del color elegido
color = colores[color_nombre]

# CSS personalizado para dar estilo a la app
estilo = f"""
<style>
.stApp {{
    background-color: {color};  /* Color de fondo según el selector */
    padding-top: 30px;          /* Espaciado superior */
    font-family: 'Segoe UI', sans-serif;  /* Fuente general */
}}

input[type="text"] {{
    font-size: 30px;            /* Tamaño del texto en la pantalla */
    text-align: right;          /* Alineación a la derecha (como una calculadora real) */
    background: #fff;           /* Fondo blanco */
    border: 2px solid #ccc;     /* Borde gris claro */
    padding: 10px;              /* Espaciado interno */
    width: 100%;                /* Ocupa todo el ancho disponible */
}}

button {{
    font-size: 24px !important; /* Tamaño del texto de los botones, forzado con !important */
    padding: 10px 0 !important; /* Espaciado vertical uniforme */
}}

</style>
"""

# Aplicamos el CSS a la app usando markdown con HTML habilitado
st.markdown(estilo, unsafe_allow_html=True)

# Título principal de la app
st.markdown("## Calculadora compacta")

# Estado inicial: se crea la variable 'expresion' en session_state si no existe
if "expresion" not in st.session_state:
    st.session_state.expresion = ""

# Función que agrega un número o símbolo a la expresión
def pulsar(valor):
    st.session_state.expresion += str(valor)

# Función que borra toda la expresión actual
def borrar():
    st.session_state.expresion = ""

# Función que evalúa la expresión matemática introducida
def calcular():
    try:
        resultado = eval(st.session_state.expresion)  # Calcula la expresión como si fuera código
        st.session_state.expresion = str(resultado)   # Guarda el resultado como texto
    except:
        st.session_state.expresion = "Error"          # Si hay un error, muestra mensaje de error

# Muestra la pantalla de resultados desactivada (para que el usuario no escriba ahí directamente)
st.text_input("Pantalla", value=st.session_state.expresion, disabled=True, label_visibility="collapsed")

# Matriz de botones como una calculadora tradicional
botones = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

# Se dibujan los botones fila por fila
for fila in botones:
    cols = st.columns(4)
    # Recorrer cada valor (val) en la fila y su indice (i) para colocar el botón correspondiente.
    for i, val in enumerate(fila): #
        if val == "=":
            cols[i].button("=", use_container_width=True, on_click=calcular)  # Botón igual ejecuta el cálculo
        elif val in ["/", "*", "-", "+"]:
            # Diccionario que reemplaza los símbolos por versiones más visuales
            texto = {"*": "×", "/": "÷", "-": "−", "+": "+"}[val]
            cols[i].button(texto, use_container_width=True, on_click=pulsar, args=(val,))  # Operadores
        else:
            cols[i].button(val, use_container_width=True, on_click=pulsar, args=(val,))    # Números y punto

# Espacio antes del botón de borrado
st.markdown(" ")

# Botón para borrar todo el contenido de la pantalla
st.button(" Borrar todo", on_click=borrar)

