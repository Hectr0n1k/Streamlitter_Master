import streamlit as st
import pandas as pd
import numpy as np

# ------------------------ CONFIGURACIÓN DE LA PÁGINA ------------------------
# Define el título y la disposición del dashboard (centrado o ancho)
st.set_page_config(page_title="Dashboard de Ventas", layout="wide")

# ------------------------ TÍTULO PRINCIPAL ------------------------
st.title("Ventas")

# ------------------------ GENERACIÓN DE DATOS SIMULADOS ------------------------
# Fijamos la semilla para que los resultados sean reproducibles
np.random.seed(42)

# Creamos fechas mensuales de enero 2022 a diciembre 2023
fechas = pd.date_range(start="2022-01-01", end="2023-12-31", freq="M")

# Categorías de productos
categorias = ["Electrónica", "Ropa", "Hogar", "Deportes"]

# Creamos un DataFrame simulando ventas para cada categoría en cada mes
data = pd.DataFrame({
    "Fecha": np.tile(fechas, len(categorias)),           # Repite fechas para cada categoría
    "Categoría": np.repeat(categorias, len(fechas)),     # Repite cada categoría por todas las fechas
    "Ventas": np.random.randint(1000, 10000, len(fechas) * len(categorias))  # Ventas aleatorias
})

# Extraemos columnas auxiliares: año y nombre del mes
data["Año"] = data["Fecha"].dt.year
data["Mes"] = data["Fecha"].dt.strftime("%b")  # 'Jan', 'Feb', etc.

# ------------------------ BARRA LATERAL: FILTROS ------------------------
st.sidebar.header("Filtros")

# Filtro de año (desplegable)
año = st.sidebar.selectbox("Selecciona el año", sorted(data["Año"].unique()))

# Filtro de categoría (puede seleccionar varias)
categoria = st.sidebar.multiselect("Selecciona categoría(s)", categorias, default=categorias)

# ------------------------ FILTRADO DE DATOS ------------------------
# Aplica los filtros seleccionados
df_filtrado = data[(data["Año"] == año) & (data["Categoría"].isin(categoria))]

# ------------------------ MÉTRICAS CLAVE ------------------------
st.subheader("🔢 Métricas principales")

# Divide la pantalla en dos columnas para mostrar métricas
col1, col2 = st.columns(2)

# Muestra ventas totales y promedio mensual en formato legible
col1.metric("Ventas totales", f"${df_filtrado['Ventas'].sum():,}")
col2.metric("Promedio por mes", f"${df_filtrado['Ventas'].mean():,.0f}")

# ------------------------ GRÁFICO DE LÍNEA ------------------------
st.subheader("📈 Ventas por mes")

# Agrupa por mes y suma ventas; reordena para que los meses estén en orden cronológico
ventas_mes = df_filtrado.groupby("Mes")["Ventas"].sum().reindex([
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
])

# Muestra gráfico de línea con los datos
st.line_chart(ventas_mes)

# ------------------------ TABLA DE DATOS DETALLADA ------------------------
st.subheader("📋 Datos detallados")

# Muestra la tabla con los datos filtrados
st.dataframe(df_filtrado.reset_index(drop=True))