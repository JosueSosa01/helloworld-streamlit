import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title(" Visualización de Datos No Relacionados al Reto")

# --- 1. Gráfico de líneas ---
st.subheader(" Ventas simuladas por trimestre (Gráfico de línea)")

df_linea = pd.DataFrame(
    np.random.randint(100, 500, size=(4, 3)),
    columns=["Producto A", "Producto B", "Producto C"],
    index=["Q1", "Q2", "Q3", "Q4"]
)

st.line_chart(df_linea)

# --- 2. Gráfico de barras ---
st.subheader(" Porcentaje de satisfacción por servicio (Gráfico de barras)")

df_barras = pd.DataFrame({
    "Servicio": ["Soporte", "Entrega", "Atención", "Postventa"],
    "Satisfacción": [85, 72, 90, 78]
})

bar_chart = alt.Chart(df_barras).mark_bar().encode(
    x="Servicio",
    y="Satisfacción",
    color="Servicio",
    tooltip=["Servicio", "Satisfacción"]
)

st.altair_chart(bar_chart, use_container_width=True)

# --- 3. Gráfico de dispersión ---
st.subheader("🔬 Relación entre calidad y precio (Gráfico de dispersión)")

df_dispersion = pd.DataFrame({
    "Precio": np.random.uniform(100, 1000, 50),
    "Calidad": np.random.uniform(1, 10, 50)
})

scatter = alt.Chart(df_dispersion).mark_circle(size=60).encode(
    x="Precio",
    y="Calidad",
    tooltip=["Precio", "Calidad"]
).interactive()

st.altair_chart(scatter, use_container_width=True)

# Pie de página
st.markdown("---")
st.caption("Datos generados artificialmente para fines de demostración.")
