import streamlit as st
import pandas as pd
import altair as alt

st.title("Datos de Videojuegos")

# DataFrame de ejemplo con texto
df = pd.DataFrame({
    'Juego': ['The Legend of Zelda', 'God of War', 'Minecraft', 'FIFA 23', 'Elden Ring'],
    'Género': ['Aventura', 'Acción', 'Sandbox', 'Deportes', 'RPG'],
    'Plataforma': ['Nintendo', 'PlayStation', 'Multiplataforma', 'Multiplataforma', 'Multiplataforma'],
    'Calificación': [9.7, 9.5, 8.9, 7.8, 9.6]
})

st.subheader("Tabla de juegos")
st.dataframe(df)

st.subheader("Calificaciones de los videojuegos")

# Gráfica de calificaciones
chart = alt.Chart(df).mark_bar().encode(
    x='Juego',
    y='Calificación',
    color='Género',
    tooltip=['Juego', 'Género', 'Calificación']
)

st.altair_chart(chart, use_container_width=True)

st.markdown("---")
st.caption("Datos ficticios creados con fines demostrativos.")
