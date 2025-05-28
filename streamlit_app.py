import streamlit as st
import time

st.set_page_config(page_title="Barras de Progreso", layout="centered")
st.title("⏳ Progreso paralelo en Streamlit")

with st.expander("ℹ️ Acerca de esta app"):
    st.write("Esta app muestra cómo manejar múltiples barras de progreso con diferentes velocidades usando `st.progress`.")

# Inicializar las barras de progreso
st.subheader("🚀 Progreso de procesos paralelos")

bar1 = st.progress(0)
bar2 = st.progress(0)
bar3 = st.progress(0)

st.write("Proceso 1: velocidad rápida ⚡")
st.write("Proceso 2: velocidad media ⏱️")
st.write("Proceso 3: velocidad lenta 🐢")

# Ciclo de actualización
for i in range(101):
    time.sleep(0.03)  # Tiempo base
    if i <= 100:
        bar1.progress(i)  # rápido
    if i % 2 == 0:
        bar2.progress(i)  # medio
    if i % 5 == 0:
        bar3.progress(i)  # lento

st.success("¡Procesos completados!")
st.balloons()
