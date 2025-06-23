import streamlit as st
import sqlite3
import aiohttp
import asyncio

# ---------- INICIALIZAR BASE DE DATOS ----------
def inicializar_db():
    conn = sqlite3.connect("productos.db")
    cur = conn.cursor()

    # Crear tabla de categorías
    cur.execute("""
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT UNIQUE NOT NULL
        )
    """)

    # Crear tabla de productos con relación a categorías
    cur.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio_eur REAL NOT NULL,
            categoria_id INTEGER NOT NULL,
            FOREIGN KEY (categoria_id) REFERENCES categorias(id)
        )
    """)

    conn.commit()
    conn.close()

inicializar_db()

# ---------- INICIO DE LA APLICACIÓN ----------
st.title("Gestión de Productos")

# 1. Crear un formulario para añadir una nueva categoría
# Consulta SQL a utilizar:
# INSERT OR IGNORE INTO categorias (nombre) VALUES (?)

# 2. Obtener la lista de categorías desde la base de datos y mostrarla en un selectbox
# Consulta SQL a utilizar:
# SELECT id, nombre FROM categorias

# Extra: añadir manualmente una opción (-1, "Mostrar todos") al principio de la lista

# 3. Crear un formulario para añadir un nuevo producto con nombre, precio en euros y categoría seleccionada
# Consulta SQL a utilizar:
# INSERT INTO productos (nombre, precio_eur, categoria_id) VALUES (?, ?, ?)

# 4. Mostrar los productos de la categoría seleccionada
# Si se seleccionó una categoría concreta:
# SELECT id, nombre, precio_eur FROM productos WHERE categoria_id = ?
# Si se seleccionó "Mostrar todos":
# SELECT id, nombre, precio_eur FROM productos

# 5. Obtener tasas de cambio EUR → USD y EUR → GBP desde esta API:
# https://open.er-api.com/v6/latest/EUR
# La respuesta JSON contiene los valores en:
# data["rates"]["USD"]
# data["rates"]["GBP"]

# Usar aiohttp y asyncio para hacer la llamada

# 6. Mostrar los productos en tabla o columnas con:
# - nombre
# - precio en EUR
# - precio en USD (calculado)
# - precio en GBP (calculado)
# - botón para eliminar producto

# Consulta SQL para eliminar:
# DELETE FROM productos WHERE id = ?



