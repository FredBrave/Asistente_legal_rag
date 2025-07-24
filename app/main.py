from fastapi import FastAPI
from app.telegram_bot import iniciar_bot

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}

@app.on_event("startup")
def startup_event():
    iniciar_bot()
