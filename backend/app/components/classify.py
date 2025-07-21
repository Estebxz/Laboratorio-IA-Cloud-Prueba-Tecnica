import streamlit as st

def show_classifier(modelo, vectorizador):
    st.subheader("Clasifica una nueva solicitud")

    with st.form("form_clasificacion"):
        entrada = st.text_area(
            "✍️ Ingresa aquí una solicitud",
            placeholder="Ejemplo: Solicito el arreglo de un poste público que no funciona en mi barrio.",
        )
        enviar = st.form_submit_button("Enviar solicitud")

    if enviar:
        if entrada.strip() == "":
            st.warning("⚠️ Por favor ingresa un texto antes de clasificar.")
        else:
            entrada_procesada = vectorizador.transform([entrada])
            prediccion = modelo.predict(entrada_procesada)[0]
            st.success("✅ Clasificación exitosa")
            st.info(f"📌 **Resultado del modelo:** {prediccion}", icon="📥")
