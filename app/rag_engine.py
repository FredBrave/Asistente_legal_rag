from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from app.config import OPENROUTER_API_KEY, OPENROUTER_MODEL, VECTOR_PATH

def cargar_qa_chain():
    try:
        print("Cargando embeddings...")
        embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

        print(f"Cargando índice desde: {VECTOR_PATH}")
        vectorstore = FAISS.load_local(
            folder_path=VECTOR_PATH,
            embeddings=embedding,
            allow_dangerous_deserialization=True
        )

        retriever = vectorstore.as_retriever()

        print(f"Cargando modelo: {OPENROUTER_MODEL}")
        llm = ChatOpenAI(
            openai_api_key=OPENROUTER_API_KEY,
            openai_api_base="https://openrouter.ai/api/v1",
            model_name=OPENROUTER_MODEL,
            temperature=0.2,
        )

        return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    except Exception as e:
        print(f"Error al cargar la cadena QA: {e}")
        raise

qa_chain = cargar_qa_chain()

def responder_pregunta(pregunta: str) -> str:
    try:
        print(f"Pregunta recibida: {pregunta}")
        respuesta = qa_chain.run(pregunta)
        print(f"Respuesta generada: {respuesta}")
        return respuesta
    except Exception as e:
        print(f"Error al responder: {e}")
        return "Hubo un error al procesar la pregunta."
