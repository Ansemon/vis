import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Estilo global
sns.set_style("darkgrid")
plt.rcParams["axes.titlesize"] = 14
plt.rcParams["axes.labelsize"] = 12

# Título de la página
st.title("📊 Análisis Descriptivo")

# Cargar datos (ajusta si tu archivo está en otro lugar o forma)
@st.cache_data
def load_data():
    return pd.read_csv("data/datos.csv")  # cambia el path si es necesario

df = load_data()

# Tabs para agrupar de 2 en 2
tabs = st.tabs(["📌 Distribuciones", "📌 Diagnósticos y Genero", "📌 Geografía y Frecuencia"])

# --- Primer Tab ---
with tabs[0]:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Distribución General de Edades")
        fig, ax = plt.subplots()
        sns.histplot(data=df, x="Edad", kde=True, bins=20, ax=ax)
        ax.set_xlabel("Edad")
        st.pyplot(fig)

    with col2:
        st.subheader("Distribución de Edad por Diagnóstico")
        fig, ax = plt.subplots()
        sns.boxplot(data=df, x="Diagnóstico", y="Edad", ax=ax)
        ax.set_ylabel("Edad")
        ax.set_xlabel("Diagnóstico")
        st.pyplot(fig)

# --- Segundo Tab ---
with tabs[1]:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Conteo por Diagnóstico y Género")
        fig, ax = plt.subplots(figsize=(7, 5))
        sns.countplot(data=df, x="Diagnóstico", hue="Genero", ax=ax)
        ax.set_ylabel("Cantidad de personas")
        st.pyplot(fig)

    with col2:
        st.subheader("Distribución por Género")
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.countplot(data=df, x="Genero", ax=ax)
        ax.set_ylabel("Cantidad")
        st.pyplot(fig)

# --- Tercer Tab ---
with tabs[2]:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Frecuencia Promedio por Departamento")
        departamento_visitas = df.groupby("Departamento")["Frecuencia_Visitas"].mean().sort_values(ascending=False)
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.heatmap(departamento_visitas.to_frame().T, cmap="Blues", annot=True, fmt=".1f", cbar=True, ax=ax)
        ax.set_xlabel("Departamento")
        st.pyplot(fig)

    with col2:
        st.subheader("Relación Edad - Frecuencia de Visitas")
        fig, ax = plt.subplots()
        sns.scatterplot(data=df, x="Edad", y="Frecuencia_Visitas", hue="Diagnóstico", ax=ax)
        ax.set_xlabel("Edad")
        ax.set_ylabel("Frecuencia de Visitas")
        st.pyplot(fig)
