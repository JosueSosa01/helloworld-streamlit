import streamlit as st

# Configuración general de la app
st.set_page_config(page_title="Encuesta con contexto", layout="centered")
st.title("📋 Encuesta de hábitos digitales y tecnológicos")

# --- VIDEOS CONTEXTUALES ---
st.markdown("### 🎥 Antes de comenzar, revisa estos videos informativos:")

# Video 1
st.video("https://www.youtube.com/watch?v=E77jLzgYk7Q")  # Puedes reemplazar con un video sobre logística o tecnología
st.caption("📌 Video 1: ¿Qué es la experiencia del usuario en entornos digitales?")

# Video 2
st.video("https://www.youtube.com/watch?v=EV3I9vP4DPA")  # Puedes reemplazar por uno sobre eficiencia en procesos
st.caption("📌 Video 2: La importancia de la tecnología en la vida diaria")

st.markdown("---")

# --- FORMULARIO DE ENCUESTA ---
with st.form("form_encuesta"):
    st.subheader("🧑 Información personal")

    nombre = st.text_input("1️⃣ ¿Cuál es tu nombre?")
    edad = st.slider("2️⃣ ¿Qué edad tienes?", 15, 80, 25)
    genero = st.radio("3️⃣ ¿Con qué género te identificas?", ["Masculino", "Femenino", "Otro", "Prefiero no decirlo"])

    st.subheader("💻 Preferencias tecnológicas")

    sistema = st.selectbox("4️⃣ ¿Qué sistema operativo usas con más frecuencia?", ["Windows", "macOS", "Linux", "Otro"])
    lenguaje = st.multiselect("5️⃣ ¿Qué lenguajes de programación has usado?", ["Python", "JavaScript", "Java", "C++", "Ninguno"])
    experiencia = st.slider("6️⃣ ¿Cuántos años de experiencia tienes programando?", 0, 20, 2)

    st.subheader("🌐 Hábitos digitales")

    redes = st.selectbox("7️⃣ ¿Cuál es tu red social favorita?", ["Instagram", "TikTok", "Facebook", "LinkedIn", "X (Twitter)"])
    horas = st.slider("8️⃣ ¿Cuántas horas al día pasas en internet?", 0, 12, 4)

    st.subheader("📝 Valoración")

    utilidad = st.radio("9️⃣ ¿Qué tan útil te pareció esta encuesta?", ["Nada útil", "Poco útil", "Útil", "Muy útil"])
    comentarios = st.text_area("🔟 ¿Tienes algún comentario adicional o sugerencia?")

    enviado = st.form_submit_button("Enviar respuestas")

# --- RESULTADO AL ENVIAR ---
if enviado:
    st.success("✅ ¡Gracias por completar la encuesta!")
    st.markdown(f"""
    ### 🧾 Resumen de tus respuestas:
    - **Nombre:** {nombre}
    - **Edad:** {edad}
    - **Género:** {genero}
    - **Sistema operativo preferido:** {sistema}
    - **Lenguajes usados:** {', '.join(lenguaje) if lenguaje else 'Ninguno'}
    - **Años de experiencia programando:** {experiencia}
    - **Red social favorita:** {redes}
    - **Horas en internet por día:** {horas}
    - **Valoración de la encuesta:** {utilidad}
    - **Comentarios:** {comentarios if comentarios else 'Ninguno'}
    """)
else:
    st.info("☝️ Completa la encuesta y haz clic en 'Enviar respuestas'.")
