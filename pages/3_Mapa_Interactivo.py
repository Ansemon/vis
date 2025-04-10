import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
from folium.plugins import MarkerCluster

# Cargar datos
@st.cache_data
def load_data():
    return pd.read_csv("data/datos.csv")  

df = load_data()

# Sidebar con filtros
st.sidebar.header("🔍 Filtros")
departamentos = st.sidebar.multiselect("Departamento", options=df["Departamento"].unique(), default=df["Departamento"].unique())
diagnosticos = st.sidebar.multiselect("Diagnóstico", options=df["Diagnóstico"].unique(), default=df["Diagnóstico"].unique())

df_filtrado = df[(df["Departamento"].isin(departamentos)) & (df["Diagnóstico"].isin(diagnosticos))]

# Calcular centro del mapa
lat_center = df_filtrado["Latitud"].mean()
lon_center = df_filtrado["Longitud"].mean()

# Crear mapa
m = folium.Map(location=[lat_center, lon_center], zoom_start=6)

# Agrupar marcadores
marker_cluster = MarkerCluster().add_to(m)

# Función para elegir color
def color_por_diagnostico(diag):
    colores = {
        "Saludable": "green",
        "Asma": "orange",
        "Diabetes": "red",
        "Hipertensión": "blue"
    }
    return colores.get(diag, "gray")

# Añadir marcadores
for _, row in df_filtrado.iterrows():
    popup_info = f"""
    <b>Edad:</b> {row['Edad']}<br>
    <b>Genero:</b> {row['Genero']}<br>
    <b>Diagnóstico:</b> {row['Diagnóstico']}<br>
    <b>Frecuencia de Visitas:</b> {row['Frecuencia_Visitas']}
    """
    folium.Marker(
        location=[row["Latitud"], row["Longitud"]],
        popup=popup_info,
        icon=folium.Icon(color=color_por_diagnostico(row["Diagnóstico"]))
    ).add_to(marker_cluster)

# Mostrar mapa
st.title("🗺️ Mapa Interactivo de Pacientes")
st.markdown("Filtra los datos desde la barra lateral para explorar la distribución geográfica.")
st_data = st_folium(m, width=900, height=600)
