import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

df = pd.read_csv("data/datos.csv")

st.title("🗺️ Georreferenciación Interactiva")

diagnostico_sel = st.selectbox("Selecciona Diagnóstico", df["Diagnóstico"].unique())
df_filtrado = df[df["Diagnóstico"] == diagnostico_sel]

st.markdown(f"Se muestran los registros con diagnóstico: **{diagnostico_sel}**")

m = folium.Map(location=[4.6, -74], zoom_start=5)

for _, row in df_filtrado.iterrows():
    folium.CircleMarker(
        location=[row["Latitud"], row["Longitud"]],
        radius=5,
        popup=(f'Departamento: {row["Departamento"]}<br>Edad: {row["Edad"]}<br>Frecuencia: {row["Frecuencia_Visitas"]}'),
        color="blue",
        fill=True,
        fill_opacity=0.7,
    ).add_to(m)

st_data = st_folium(m, width=800, height=500)
