import streamlit as st
from PIL import Image

st.title("📘 Contexto del Proyecto")

st.markdown("""
Este proyecto presenta un análisis exploratorio de datos de salud provenientes de distintas regiones de **Colombia**, con el objetivo de comprender mejor la distribución geográfica y demográfica de diagnósticos clínicos comunes. El conjunto de datos contiene registros que incluyen información como la **edad**, el **género**, el **departamento** de residencia, el **diagnóstico** médico registrado y la **frecuencia de visitas** realizadas por cada paciente.

El análisis se desarrolla en tres secciones principales. En la sección de **Análisis Descriptivo**, se exploran visualmente las variables del dataset para identificar patrones generales, como la distribución de diagnósticos por edad o la prevalencia por género. Esto permite una primera aproximación a la caracterización de la población incluida.

En la sección de **Mapa Interactivo**, se presentan los datos georreferenciados mediante un mapa dinámico que permite filtrar por diagnóstico y visualizar en qué regiones del país se concentran los casos. Esta herramienta es útil para detectar zonas de mayor incidencia de ciertas condiciones de salud, lo que puede ser relevante para la planificación de recursos médicos o campañas de prevención.

El objetivo final es construir una base visual y analítica que facilite la interpretación de los datos y permita a instituciones o investigadores tomar decisiones fundamentadas en evidencias espaciales y demográficas.
""")

imagen = Image.open("image.png")
st.image(imagen, caption="Mapa de Colombia", width=600)