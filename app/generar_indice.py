import os
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.config import VECTOR_PATH

def cargar_documentos_desde_carpeta(carpeta: str):
    documentos = []
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

    for archivo in os.listdir(carpeta):
        if archivo.endswith(".pdf"):
            path = os.path.join(carpeta, archivo)
            print(f"📄 Procesando: {archivo}")
            loader = PyPDFLoader(path)
            docs = loader.load()
            chunks = splitter.split_documents(docs)
            documentos.extend(chunks)

    return documentos

def generar_indice():
    print("Buscando documentos en carpeta 'data/'...")
    documentos = cargar_documentos_desde_carpeta("data")

    if not documentos:
        print("No se encontraron documentos PDF en la carpeta 'data/'.")
        return

    print(f"Generando embeddings para {len(documentos)} fragmentos...")
    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    print(f"Guardando índice en '{VECTOR_PATH}'...")
    vectorstore = FAISS.from_documents(documentos, embedding)
    vectorstore.save_local(VECTOR_PATH)

    print("Índice FAISS generado correctamente.")

if __name__ == "__main__":
    generar_indice()