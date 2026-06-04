"""
Ingesta de documentos para el sistema RAG (Vector RAG base).

Carga los documentos .txt de la carpeta documentos/, los divide en chunks
con solapamiento, genera embeddings con OpenAI y los almacena en ChromaDB.

Uso:
    python ingesta.py

Requiere un archivo .env con OPENAI_API_KEY (ver .env.example).
"""

import os
from dotenv import load_dotenv

# NOTA: usamos los paquetes "standalone" modernos de LangChain en lugar de
# langchain_community.vectorstores (que está en proceso de deprecación).
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

# Cargar variables de entorno
load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("No se encontró OPENAI_API_KEY. Crea un archivo .env (ver .env.example).")


def cargar_documentos(ruta_documentos: str):
    """Carga todos los documentos .txt de la carpeta indicada."""
    loader = DirectoryLoader(
        ruta_documentos,
        glob="**/*.txt",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
    )
    documentos = loader.load()
    print(f"Documentos cargados: {len(documentos)}")
    for doc in documentos:
        print(f"  - {doc.metadata['source']} ({len(doc.page_content)} caracteres)")
    return documentos


def dividir_documentos(documentos):
    """Divide los documentos en chunks con solapamiento."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=30,
        length_function=len,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    chunks = text_splitter.split_documents(documentos)
    print(f"Chunks generados: {len(chunks)}")
    media = sum(len(c.page_content) for c in chunks) // len(chunks)
    print(f"Tamaño medio de chunk: {media} caracteres")
    return chunks


def crear_base_vectorial(chunks, ruta_db: str = "./chroma_db"):
    """Genera embeddings y almacena en ChromaDB."""
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=ruta_db,
        collection_name="empresa_docs",
    )
    print(f"Base vectorial creada en: {ruta_db}")
    print(f"Vectores almacenados: {vectorstore._collection.count()}")
    return vectorstore


if __name__ == "__main__":
    print("=" * 50)
    print("INGESTA DE DOCUMENTOS - Sistema RAG")
    print("=" * 50)

    documentos = cargar_documentos("./documentos")
    chunks = dividir_documentos(documentos)

    print("\nEjemplo de chunk:")
    print(f"  Contenido: {chunks[0].page_content[:150]}...")
    print(f"  Metadata: {chunks[0].metadata}")

    crear_base_vectorial(chunks)
    print("\nIngesta completada con éxito.")
