import os
from PyPDF2 import PdfReader

def extraer_texto(ruta: str) -> str:
    if ruta.endswith(".pdf"):
        reader = PdfReader(ruta)
        return "\n".join([page.extract_text() or "" for page in reader.pages])
    elif ruta.endswith(".txt"):
        with open(ruta, "r", encoding="utf-8") as f:
            return f.read()
    return ""