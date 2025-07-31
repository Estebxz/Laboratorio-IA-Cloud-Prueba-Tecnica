import streamlit as st

def show_classifier(modelo, vectorizador):
    st.subheader("🤖 Clasificador de Solicitudes de Violencia de Género")

    with st.form("form_clasificacion"):
        entrada = st.text_area(
            "✍️ Ingresa aquí una solicitud",
            placeholder="Ejemplo: Necesito ayuda con una situación de violencia de género.",
            height=150,
        )
        enviar = st.form_submit_button("Enviar solicitud")

    if enviar:
        if not entrada.strip():
            st.warning("⚠️ Por favor ingresa un texto antes de clasificar.")
        else:
            entrada_procesada = vectorizador.transform([entrada])
            prediccion = modelo.predict(entrada_procesada)[0]

            st.success("✅ Clasificación exitosa")
            st.markdown(f"📌 **Resultado del modelo:** `{prediccion}`")

            if hasattr(modelo, "predict_proba"):
                proba = modelo.predict_proba(entrada_procesada)[0]
                etiquetas = modelo.classes_
                proba_dict = dict(zip(etiquetas, proba))
                st.write("### 🔍 Probabilidades por clase")
                st.json(proba_dict)