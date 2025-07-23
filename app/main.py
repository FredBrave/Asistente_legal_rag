from fastapi import FastAPI
from multiprocessing import Process
from app.telegram_bot import iniciar_bot

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}

# Ejecuta el bot como un proceso separado
if __name__ != "__main__":
    # Esto es necesario para evitar que el bot se ejecute varias veces en recarga
    # por el --reload de Uvicorn
    pass
else:
    bot_process = Process(target=iniciar_bot, daemon=True)
    bot_process.start()
