import streamlit as st
import pandas as pd
import joblib
import os

from components.header import show_header
from components.preview import show_preview
from components.graphic import show_graphic
from components.classify import show_classifier
# Configurar la app
st.set_page_config(
    page_title="Clasificador de Solicitudes Ciudadanas",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Cargar modelo y vectorizador
model_path = os.path.join(os.path.dirname(__file__), "models", "model.pkl")
modelo = joblib.load(model_path)
vectorizer_path = os.path.join(os.path.dirname(__file__), "models", "vectorizer.pkl")
vectorizador = joblib.load("models/vectorizer.pkl")

# Cargar datos
@st.cache_data
def cargar_datos():
    return pd.read_csv("data/solicitudes_ciudadanas.csv")

df = cargar_datos()

# Mostrar secciones
show_header()
col1, col2 = st.columns([1, 2])
with col1:
    show_preview(df)
with col2:
    show_graphic(df)

st.divider()
show_classifier(modelo, vectorizador)

st.divider()
st.caption("Desarrollado con 💻 por Joan")
