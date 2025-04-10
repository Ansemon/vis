import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Mi App de Datos", layout="wide")

with st.sidebar:
    selected = option_menu(
        menu_title="Menú",
        options=["Contexto", "Análisis Descriptivo", "Mapa Interactivo"],
        icons=["info-circle", "bar-chart", "map"],
        menu_icon="cast",
        default_index=0,
    )

if selected == "Contexto":
    st.switch_page("pages/1_Contexto.py")
elif selected == "Análisis Descriptivo":
    st.switch_page("pages/2_Analisis_Descriptivo.py")
elif selected == "Mapa Interactivo":
    st.switch_page("pages/3_Mapa_Interactivo.py")
