import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Configuración de página
st.set_page_config(layout="wide", page_title="App con 5 Secciones", page_icon="🧩")

# Título de la app
st.title("🎯 App interactiva con 5 secciones diferentes")

# Expander informativo
with st.expander("ℹ️ Acerca de esta app"):
    st.write("Esta app muestra cómo organizar el contenido en Streamlit en un layout de columnas con diferentes elementos visuales e interactivos.")

# Sección de entrada lateral
st.sidebar.header("🔧 Opciones de entrada")
nombre = st.sidebar.text_input("¿Cuál es tu nombre?")
color = st.sidebar.selectbox("Elige un color favorito:", ["", "Rojo", "Azul", "Verde", "Amarillo"])
mostrar = st.sidebar.button("Mostrar saludo")

# Layout de 5 secciones
col1, col2, col3 = st.columns(3)
col4, col5 = st.columns(2)

# Sección 1 - Texto dinámico
with col1:
    st.subheader("👋 Saludo")
    if mostrar and nombre:
        st.success(f"¡Hola, {nombre}!")
    else:
        st.info("Escribe tu nombre y presiona el botón para saludar.")

# Sección 2 - Selección
with col2:
    st.subheader("🎨 Color favorito")
    if color:
        st.write(f"Tu color favorito es **{color}**")
    else:
        st.warning("Aún no seleccionas un color.")

# Sección 3 - Gráfico
with col3:
    st.subheader("📊 Gráfico de barras")
    data = pd.DataFrame({
        "Categoría": ["A", "B", "C", "D"],
        "Valor": np.random.randint(10, 100, 4)
    })
    chart = alt.Chart(data).mark_bar().encode(
        x="Categoría", y="Valor", color="Categoría", tooltip=["Categoría", "Valor"]
    )
    st.altair_chart(chart, use_container_width=True)

# Sección 4 - Imagen
with col4:
    st.subheader("🖼️ Imagen destacada")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/React-icon.svg/1024px-React-icon.svg.png", width=200)
    st.caption("Logo de React - Imagen externa usada como ejemplo.")

# Sección 5 - Botón extra
with col5:
    st.subheader("🔘 Acción extra")
    if st.button("¿Te gusta Streamlit?"):
        st.balloons()
        st.success("¡Nos alegra saberlo! 🎈")

# Pie de página
st.markdown("---")
st.caption("App creada por Josué · Todos los datos son de prueba.")
