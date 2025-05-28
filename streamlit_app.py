import streamlit as st

st.title("🚚 Opciones de Optimización Logística")

st.write("Selecciona las estrategias que aplicarías para reducir los costos de envío:")

# Checkboxes relacionadas al reto
uso_rutas = st.checkbox(" Optimizar rutas con menor distancia")
consolidacion = st.checkbox(" Consolidar pedidos por zona")
horarios = st.checkbox(" Establecer ventanas de entrega eficientes")
proveedores = st.checkbox(" Usar proveedores locales")
almacenamiento = st.checkbox("Reubicar centros de distribución")

# Mostrar selección
st.subheader(" Estrategias seleccionadas:")

if uso_rutas:
    st.write("- Se seleccionó **optimizar rutas** para minimizar distancia recorrida.")

if consolidacion:
    st.write("- Se eligió **consolidar entregas por zona** para reducir viajes.")

if horarios:
    st.write("- Se propone **establecer horarios óptimos de entrega**.")

if proveedores:
    st.write("- Se considera usar **proveedores más cercanos** al cliente final.")

if almacenamiento:
    st.write("- Se plantea **reubicar almacenes** estratégicamente.")

# Feedback final
if not (uso_rutas or consolidacion or horarios or proveedores or almacenamiento):
    st.info("Selecciona al menos una estrategia para continuar con el análisis.")
