from fastapi import FastAPI
from pydantic import BaseModel
import joblib

modelo = joblib.load("./models/model.pkl")
vectorizer = joblib.load("./models/vectorizer.pkl")

app = FastAPI()

class Solicitud(BaseModel):
    texto: str

@app.post("/clasificar/")
def clasificar_solicitud(solicitud: Solicitud):
    texto = solicitud.texto
    vector = vectorizer.transform([texto])
    prediccion = modelo.predict(vector)
    return {"tipo": prediccion[0]}