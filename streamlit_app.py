import streamlit as st

st.title('🎨 Personalización del Tema en Streamlit')

st.write('Este es el contenido del archivo `.streamlit/config.toml` que define el tema de esta app:')
st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""", language='toml')

number = st.sidebar.slider('Selecciona un número:', 0, 10, 5)
st.write('Número seleccionado:', number)

