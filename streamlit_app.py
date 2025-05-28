import streamlit as st
from datetime import time, datetime

st.title("🎯 Encuesta de Preferencias del Usuario")
st.markdown("Por favor ajusta los siguientes sliders para registrar tu información:")

# Slider 1: Edad
st.subheader("🧓 ¿Cuál es tu edad?")
edad = st.slider("Selecciona tu edad", min_value=0, max_value=100, value=25)
st.write(f"Tienes {edad} años.")

# Slider 2: Horario de comida
st.subheader("🍽️ ¿A qué hora sueles comer?")
comida = st.slider("Elige un horario", value=time(14, 0))
st.write(f"Tu horario preferido para comer es: {comida}")

# Slider 3: Rango de presupuesto para videojuegos
st.subheader("🎮 ¿Cuál es tu rango de presupuesto mensual para videojuegos?")
presupuesto = st.slider("Selecciona el rango", 0, 5000, (1000, 3000))
st.write(f"Tu presupuesto mensual para videojuegos está entre ${presupuesto[0]} y ${presupuesto[1]} MXN.")

# Slider 4: Fecha y hora de última compra
st.subheader("🛍️ ¿Cuándo hiciste tu última compra en línea?")
ultima_compra = st.slider("Elige fecha y hora", value=datetime(2025, 1, 1, 15, 0), format="DD/MM/YY - hh:mm")
st.write(f"Tu última compra fue el {ultima_compra.strftime('%d/%m/%Y a las %H:%M')} hrs.")

st.markdown("---")
st.caption("Todos los datos presentados son simulados con fines de ejemplo.")
