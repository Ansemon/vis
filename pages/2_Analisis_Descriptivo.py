import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

df = pd.read_csv("data/datos.csv")

st.title("📊 Análisis Descriptivo")

st.subheader("Vista general de los datos")
st.dataframe(df)

st.subheader("📈 Edad promedio por diagnóstico")
edad_prom = df.groupby("Diagnóstico")["Edad"].mean().reset_index()
fig = px.bar(edad_prom, x="Diagnóstico", y="Edad", title="Edad Promedio por Diagnóstico")
st.plotly_chart(fig)

st.subheader("📊 Distribución de Frecuencia de Visitas")
fig2, ax = plt.subplots()
df["Frecuencia_Visitas"].hist(bins=10, ax=ax)
st.pyplot(fig2)

st.subheader("👫 Conteo por Género")
genero = df["Genero"].value_counts()
st.bar_chart(genero)
