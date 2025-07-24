from fastapi import APIRouter, UploadFile, File, HTTPException
from app.documentos.service import guardar_documento, listar_documentos, procesar_documento

router = APIRouter(prefix="/documentos", tags=["Documentos"])

@router.post("/subir")
async def subir_documento(file: UploadFile = File(...)):
    if not file.filename.endswith((".pdf", ".txt")):
        raise HTTPException(status_code=400, detail="Formato no soportado")
    path = await guardar_documento(file)
    procesar_documento(path)
    return {"mensaje": f"Documento {file.filename} cargado y procesado."}

@router.get("/listar")
def ver_documentos():
    return listar_documentos()
