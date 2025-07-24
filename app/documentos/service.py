import os
from pathlib import Path
from typing import List
from fastapi import UploadFile
from app.documentos.utils import extraer_texto
from app.rag_engine import actualizar_indice_con_texto

DIRECTORIO_DOCUMENTOS = "data/documentos"

os.makedirs(DIRECTORIO_DOCUMENTOS, exist_ok=True)

async def guardar_documento(file: UploadFile) -> str:
    path = os.path.join(DIRECTORIO_DOCUMENTOS, file.filename)
    with open(path, "wb") as f:
        content = await file.read()
        f.write(content)
    return path

def listar_documentos() -> List[str]:
    return os.listdir(DIRECTORIO_DOCUMENTOS)

def procesar_documento(ruta: str):
    texto = extraer_texto(ruta)
    actualizar_indice_con_texto(texto)
