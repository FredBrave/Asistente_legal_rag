from fastapi import APIRouter, UploadFile, File, HTTPException
from app.documentos.service import guardar_documento, listar_documentos, procesar_documento

router = APIRouter(prefix="/documentos", tags=["Gestion de Documentos"])

@router.post("/subir", summary="Sube un documento legal", description="Permite subir archivos .pdf o .txt y una vez subidos son indexados")
async def subir_documento(file: UploadFile = File(...)):
    if not file.filename.endswith((".pdf", ".txt")):
        raise HTTPException(status_code=400, detail="Formato no soportado")
    path = await guardar_documento(file)
    procesar_documento(path)
    return {"mensaje": f"Documento {file.filename} cargado y procesado."}

@router.get("/listar", summary="Lista todos los documentos guardados", description="Lista todos los documentos subidos dentro del servidor, los cuales pueden ser ")
def ver_documentos():
    return listar_documentos()
