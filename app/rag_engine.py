from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from app.config import OPENROUTER_API_KEY, OPENROUTER_MODEL, VECTOR_PATH

def cargar_qa_chain():
    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.load_local(VECTOR_PATH, embedding)
    retriever = vectorstore.as_retriever()

    llm = ChatOpenAI(
        openai_api_key=OPENROUTER_API_KEY,
        openai_api_base="https://openrouter.ai/api/v1",
        model_name=OPENROUTER_MODEL,
        temperature=0.2,
    )

    return RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

qa_chain = cargar_qa_chain()

def responder_pregunta(pregunta: str) -> str:
    return qa_chain.run(pregunta)