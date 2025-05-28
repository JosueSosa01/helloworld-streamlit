import streamlit as st

st.title("📋 Encuesta de preferencias del usuario")

# Pregunta 1
color = st.selectbox("🎨 ¿Cuál es tu color favorito?", ("Azul", "Rojo", "Verde", "Negro", "Amarillo"))
st.write("Elegiste:", color)

# Pregunta 2
comida = st.selectbox("🍕 ¿Cuál es tu tipo de comida preferida?", ("Italiana", "Mexicana", "Japonesa", "India", "Vegana"))
st.write("Te gusta la comida:", comida)

# Pregunta 3
plataforma = st.selectbox("🎮 ¿Qué consola prefieres para jugar videojuegos?", ("PlayStation", "Xbox", "Nintendo Switch", "PC", "Ninguna"))
st.write("Prefieres jugar en:", plataforma)

# Pregunta 4
viaje = st.selectbox("🌍 ¿Qué destino elegirías para tus próximas vacaciones?", ("Playa", "Montaña", "Ciudad", "Bosque", "Extranjero"))
st.write("Tu destino ideal es:", viaje)

# Pregunta 5
mascota = st.selectbox("🐾 ¿Cuál es tu mascota favorita?", ("Perro", "Gato", "Ave", "Pez", "Otro"))
st.write("Tu mascota favorita es:", mascota)

st.markdown("---")
st.caption("Gracias por completar esta encuesta ficticia 😊")
