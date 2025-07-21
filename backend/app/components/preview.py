import streamlit as st

def show_preview(df):    
    st.subheader("Vista previa")
    st.dataframe(df.head(50), use_container_width=True)
    st.write("")
    st.title(f"{len(df)}")
    st.caption("Total de solicitudes registradas")