import streamlit as st

st.set_page_config(page_title="Encuesta de Usuario", layout="centered")
st.title("📋 Encuesta de satisfacción del usuario")

st.subheader("Por favor, responde las siguientes 10 preguntas:")

with st.form("form_encuesta"):
    st.markdown("### 🧑 Datos personales")

    nombre = st.text_input("1️⃣ ¿Cuál es tu nombre?")
    edad = st.slider("2️⃣ ¿Qué edad tienes?", 15, 80, 25)
    genero = st.radio("3️⃣ ¿Con qué género te identificas?", ["Masculino", "Femenino", "Otro", "Prefiero no decirlo"])

    st.markdown("### 💻 Preferencias tecnológicas")

    sistema = st.selectbox("4️⃣ ¿Qué sistema operativo usas con más frecuencia?", ["Windows", "macOS", "Linux", "Otro"])
    lenguaje = st.multiselect("5️⃣ ¿Qué lenguajes de programación has usado?", ["Python", "JavaScript", "Java", "C++", "Ninguno"])
    experiencia = st.slider("6️⃣ ¿Cuántos años de experiencia tienes programando?", 0, 20, 2)

    st.markdown("### 🌐 Hábitos digitales")

    redes = st.selectbox("7️⃣ ¿Cuál es tu red social favorita?", ["Instagram", "TikTok", "Facebook", "LinkedIn", "X (Twitter)"])
    horas = st.slider("8️⃣ ¿Cuántas horas al día pasas en internet?", 0, 12, 4)

    st.markdown("### 📝 Valoración")

    utilidad = st.radio("9️⃣ ¿Qué tan útil te pareció esta encuesta?", ["Nada útil", "Poco útil", "Útil", "Muy útil"])
    comentarios = st.text_area("🔟 ¿Tienes algún comentario adicional o sugerencia?")

    enviado = st.form_submit_button("Enviar respuestas")

if enviado:
    st.success("✅ ¡Gracias por completar la encuesta!")
    st.markdown(f"""
    ### 🧾 Resumen de respuestas:
    - Nombre: `{nombre}`
    - Edad: `{edad}`
    - Género: `{genero}`
    - Sistema operativo: `{sistema}`
    - Lenguajes usados: `{', '.join(lenguaje) if lenguaje else 'Ninguno'}`
    - Años de experiencia: `{experiencia}`
    - Red social favorita: `{redes}`
    - Horas en internet: `{horas}`
    - Valoración: `{utilidad}`
    - Comentarios: `{comentarios if comentarios else 'Ninguno'}`
    """)
else:
    st.info("☝️ Completa la encuesta y haz clic en 'Enviar respuestas'.")
