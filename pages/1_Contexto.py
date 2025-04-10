import streamlit as st
from PIL import Image

st.title("📘 Contexto del Proyecto")
st.markdown("""
Este proyecto analiza datos de salud geolocalizados por departamento. Se incluyen variables como edad, género, diagnóstico y frecuencia de visitas.
""")

st.image("https://cdn.pixabay.com/photo/2017/06/09/00/24/colombia-2381321_960_720.png", caption="Mapa de Colombia", use_column_width=True)
