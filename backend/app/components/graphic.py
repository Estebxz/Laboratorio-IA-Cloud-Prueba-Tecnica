import streamlit as st
import pandas as pd
import plotly.express as px

def df():
    return pd.read_csv("data/Casos_de_violencia_de_genero_20250731.csv")

def show_graphic(df):
    st.subheader("Distribución por Tipo de Seguridad Social")
    conteo = df["TIP_SS"].value_counts().reset_index()
    conteo.columns = ["Tipo de Seguridad Social", "Cantidad"]
    conteo = conteo.sort_values("Cantidad", ascending=False)

    fig = px.bar(
        conteo,
        x="Tipo de Seguridad Social",
        y="Cantidad",
        color="Tipo de Seguridad Social",
        text="Cantidad",
        color_discrete_sequence=px.colors.qualitative.Set2,
    )

    fig.update_layout(
        title=dict(text="📈 Casos por Tipo de Seguridad Social", x=0.5, font=dict(size=18)),
        xaxis_title="Tipo de Seguridad Social",
        yaxis_title="Cantidad",
        bargap=0.3,
        showlegend=False,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(size=14),
    )

    fig.update_traces(textposition="outside")

    st.plotly_chart(fig, use_container_width=True)