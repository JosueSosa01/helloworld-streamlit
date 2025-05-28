import streamlit as st

st.title("Encuesta de selección múltiple")

# Pregunta 1
colores = st.multiselect(
    " ¿Cuáles son tus colores favoritos?",
    ['Verde', 'Amarillo', 'Rojo', 'Azul', 'Negro'],
    default=['Rojo', 'Azul', 'Verde']
)
st.write("Colores elegidos:", colores)

# Pregunta 2
comidas = st.multiselect(
    "¿Qué tipos de comida te gustan más?",
    ['Mexicana', 'Italiana', 'Japonesa', 'India', 'Vegana'],
    default=['Mexicana', 'Japonesa', 'Italiana']
)
st.write("Comidas seleccionadas:", comidas)

# Pregunta 3
musica = st.multiselect(
    "🎵 ¿Qué géneros musicales escuchas frecuentemente?",
    ['Pop', 'Rock', 'Clásica', 'Reggaetón', 'Jazz'],
    default=['Pop', 'Rock', 'Jazz']
)
st.write("Géneros musicales favoritos:", musica)

# Pregunta 4
series = st.multiselect(
    " ¿Qué tipos de series ves con más frecuencia?",
    ['Drama', 'Comedia', 'Documental', 'Acción', 'Suspenso'],
    default=['Comedia', 'Acción', 'Suspenso']
)
st.write("Tipos de series elegidos:", series)

# Pregunta 5
actividades = st.multiselect(
    " ¿Qué actividades disfrutas en tu tiempo libre?",
    ['Leer', 'Hacer ejercicio', 'Jugar videojuegos', 'Ver películas', 'Salir con amigos'],
    default=['Leer', 'Ver películas', 'Jugar videojuegos']
)
st.write("Actividades seleccionadas:", actividades)

st.markdown("---")
st.caption("Gracias por tu participación. Esta encuesta es ficticia ")
