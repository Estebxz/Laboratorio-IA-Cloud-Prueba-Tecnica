<a name="readme-top"></a>

<div align="center">

[![Stars](https://img.shields.io/github/stars/Estebxz/Proyecto-capstone.svg?style=for-the-badge)](https://github.com/Estebxz/Proyecto-capstone/stargazers)
[![Issues](https://img.shields.io/github/issues/Estebxz/Proyecto-capstone.svg?style=for-the-badge)](https://github.com/Estebxz/Proyecto-capstone/issues)

<p align="center">
    <img src="https://i.postimg.cc/1tvvzvX5/0bc2137b-72de-41e9-bfe9-9437e89571aa.png" alt="Captura de pantalla" width="300"/>
</p>

<h3 align="center">Clasificador de Solicitudes Ciudadanas con IA</h3>

<p align="center">
  Aplicación interactiva para clasificar automáticamente solicitudes ciudadanas <em>(PQR, QUEJAS Y FELICITACIONES)<em/> usando Machine Learning e interfaces amigables en Streamlit.
  <br />
  <a href="https://github.com/tuusuario/solicitudes-ciudadanas/issues">Reportar un error</a>
  ·
  <a href="https://github.com/tuusuario/solicitudes-ciudadanas/issues">Sugerir funcionalidad</a>
</p>

</div>

---

## 🧠 Descripción del proyecto

Esta herramienta web permite clasificar automáticamente solicitudes ciudadanas en categorías específicas utilizando modelos de aprendizaje automático previamente entrenados. Está pensada para agilizar la gestión de PQRs (Peticiones, Quejas y Reclamos) mediante una interfaz sencilla e intuitiva construida con Streamlit.

---

## 📸 Capturas de pantalla

<p align="center">
  <img src="https://i.postimg.cc/ZnYWKLgH/303shots-so.png" alt="Captura de pantalla" width="800"/>
</p>

<p align="right">(<a href="#readme-top">volver arriba</a>)</p>

---

## 📦 Características principales

- **Clasificación automática** de texto en tiempo real.
- **Interfaz visual con gráficas interactivas** usando Plotly.
- **Visualización de datos** cargados desde un CSV.
- **Componentización del código** para mayor escalabilidad.
---

## 🚀 Para empezar

### ✅ Pre-requisitos

Asegúrate de tener instalado lo siguiente:

- Python 3.10 o superior
- pip (instalador de paquetes de Python)
- Git
- Docker (opcional)

### 🔧 Instalación

1. Clona el repositorio:

```bash
git clone https://github.com/Estebxz/Proyecto-capstone/.git
cd .\backend\
cd .\app\
streamlit run app.py
```
2. Creacion de imagen y contenedor Docker(opcional)
```
docker build -t pqr-ai .
docker run -p 8501:8501 pqr-ai
```
<p align="right">(<a href="#readme-top">volver arriba</a>)</p>
