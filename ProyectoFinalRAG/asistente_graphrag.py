"""
Asistente RAG para documentación de empresa (Vector RAG base).

Carga la base vectorial generada por ingesta.py, recupera los chunks más
relevantes para cada pregunta y genera respuestas contextualizadas con un LLM.
Incluye una interfaz CLI interactiva.

Uso:
    python ingesta.py     # solo la primera vez, para indexar
    python asistente.py   # modo interactivo

Requiere un archivo .env con OPENAI_API_KEY (ver .env.example).
"""

import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("No se encontró OPENAI_API_KEY. Crea un archivo .env (ver .env.example).")


def cargar_base_vectorial(ruta_db: str = "./chroma_db"):
    """Carga la base vectorial existente."""
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
    vectorstore = Chroma(
        persist_directory=ruta_db,
        embedding_function=embeddings,
        collection_name="empresa_docs",
    )
    print(f"Base vectorial cargada: {vectorstore._collection.count()} vectores")
    return vectorstore


def crear_cadena_rag(vectorstore):
    """Crea la cadena RAG con LCEL (LangChain Expression Language)."""
    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3},
    )

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

    template = ChatPromptTemplate.from_messages([
        ("system", """Eres el asistente virtual de TechCorp, especializado en responder
preguntas sobre la documentación interna de la empresa.

INSTRUCCIONES:
- Responde SOLO con información que esté en el contexto proporcionado.
- Si la información no está en el contexto, responde exactamente: "No dispongo de
  información sobre ese tema en la documentación de la empresa. Te recomiendo
  contactar con el departamento correspondiente."
- NO inventes políticas, procedimientos ni datos.
- Sé claro, conciso y profesional. Indica el documento fuente cuando sea posible.

CONTEXTO DE DOCUMENTOS INTERNOS:
{context}"""),
        ("human", "{question}"),
    ])

    def formatear_docs(docs):
        return "\n\n---\n\n".join(
            f"[Fuente: {doc.metadata.get('source', 'desconocida')}]\n{doc.page_content}"
            for doc in docs
        )

    cadena = (
        {"context": retriever | formatear_docs, "question": RunnablePassthrough()}
        | template
        | llm
        | StrOutputParser()
    )
    return cadena, retriever


def main():
    """Ejecuta el asistente en modo interactivo por CLI."""
    print("=" * 50)
    print("ASISTENTE RAG - TechCorp")
    print("=" * 50)
    print("Escribe tu pregunta sobre la documentación de la empresa.")
    print("Escribe 'salir' para terminar.\n")

    vectorstore = cargar_base_vectorial()
    cadena, retriever = crear_cadena_rag(vectorstore)

    while True:
        pregunta = input("\nTú: ").strip()
        if pregunta.lower() in ["salir", "exit", "quit", "q"]:
            print("\n¡Hasta luego!")
            break
        if not pregunta:
            print("Por favor, escribe una pregunta.")
            continue

        try:
            docs = retriever.invoke(pregunta)
            print(f"\n[Documentos recuperados: {len(docs)}]")
            for i, doc in enumerate(docs, 1):
                fuente = doc.metadata.get("source", "desconocida")
                print(f"  {i}. {fuente} - {doc.page_content[:80]}...")

            respuesta = cadena.invoke(pregunta)
            print(f"\nAsistente: {respuesta}")
        except Exception as e:
            print(f"\nError al procesar la pregunta: {e}")


if __name__ == "__main__":
    main()
