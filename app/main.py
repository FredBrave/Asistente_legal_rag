from fastapi import FastAPI
from app.telegram_bot import iniciar_bot
from app.documentos.controller import router as documentos_router
app = FastAPI()

app.include_router(documentos_router)

@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}

@app.on_event("startup")
def startup_event():
    iniciar_bot()