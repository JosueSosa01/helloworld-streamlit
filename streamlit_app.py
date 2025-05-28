import streamlit as st
import pandas as pd

st.set_page_config(page_title="📂 Comparación de Archivos CSV", layout="centered")
st.title("📊 Carga y análisis de dos archivos CSV diferentes")

st.markdown("Por favor, sube dos archivos CSV distintos para analizarlos por separado.")

# Primer archivo
st.subheader("📁 Archivo 1: Ventas")
archivo_ventas = st.file_uploader("Selecciona el archivo de ventas", type=["csv"], key="ventas")

# Segundo archivo
st.subheader("📁 Archivo 2: Clientes")
archivo_clientes = st.file_uploader("Selecciona el archivo de clientes", type=["csv"], key="clientes")

# Mostrar datos del archivo 1
if archivo_ventas is not None:
    df_ventas = pd.read_csv(archivo_ventas)
    st.success("✅ Archivo de ventas cargado correctamente")
    st.write("### Vista previa del archivo de ventas:")
    st.dataframe(df_ventas)
    st.write("### Estadísticas descriptivas de ventas:")
    st.write(df_ventas.describe())
else:
    st.info("☝️ Por favor sube el archivo de ventas.")

# Mostrar datos del archivo 2
if archivo_clientes is not None:
    df_clientes = pd.read_csv(archivo_clientes)
    st.success("✅ Archivo de clientes cargado correctamente")
    st.write("### Vista previa del archivo de clientes:")
    st.dataframe(df_clientes)
    st.write("### Estadísticas descriptivas de clientes:")
    st.write(df_clientes.describe())
else:
    st.info("☝️ Por favor sube el archivo de clientes.")
