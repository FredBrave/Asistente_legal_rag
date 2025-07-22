from fastapi import FastAPI
import threading

app = FastAPI()

@app.get("/")
def home():
    return {"mensaje": "Asistente legal activo"}

# Ejecutar el bot de Telegram en un hilo paralelo
threading.Thread(target=iniciar_bot, daemon=True).start()