"""
Asistente GraphRAG sobre Neo4j (extra/bonificación de la sesión 3).

Usa VectorCypherRetriever: combina búsqueda vectorial sobre los chunks con una
traversal Cypher que recupera el contexto del grafo vecino (entidades y
relaciones extraídas de cada chunk). Sirve para comparar la calidad de las
respuestas frente al Vector RAG base, sobre todo en preguntas multi-hop.

Uso:
    python ingesta_graphrag.py      # primero, para construir el grafo
    python asistente_graphrag.py    # después, para preguntar

Requiere en .env: OPENAI_API_KEY, NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD.
"""

import os
import neo4j
from dotenv import load_dotenv
from neo4j_graphrag.embeddings import OpenAIEmbeddings
from neo4j_graphrag.llm import OpenAILLM
from neo4j_graphrag.retrievers import VectorCypherRetriever
from neo4j_graphrag.generation import GraphRAG

load_dotenv()

driver = neo4j.GraphDatabase.driver(
    os.environ["NEO4J_URI"],
    auth=(os.environ["NEO4J_USERNAME"], os.environ["NEO4J_PASSWORD"]),
)

# Traversal: para cada chunk recuperado, devolvemos también las entidades
# extraídas de él y sus relaciones inmediatas (el "vecindario" en el grafo).
# Nota: la relación chunk<-entidad la crea SimpleKGPipeline como FROM_CHUNK.
# Si tu versión usa otro nombre, compruébalo con:
#   MATCH ()-[r]->() RETURN DISTINCT type(r)
retrieval_query = """
MATCH (node)<-[:FROM_CHUNK]-(e)
OPTIONAL MATCH (e)-[r]-(o)
RETURN node.text AS chunk_text,
       collect(DISTINCT e.name) AS entidades,
       collect(DISTINCT type(r) + ': ' + coalesce(o.name, '')) AS relaciones
"""

retriever = VectorCypherRetriever(
    driver=driver,
    index_name="chunk_embeddings",
    retrieval_query=retrieval_query,
    embedder=OpenAIEmbeddings(model="text-embedding-3-small"),
)

# OJO: el LLM que GENERA la respuesta NO debe usar response_format json_object,
# o dará un 400 ("messages must contain the word 'json'").
llm = OpenAILLM(model_name="gpt-4o-mini", model_params={"temperature": 0.1})
rag = GraphRAG(retriever=retriever, llm=llm)


if __name__ == "__main__":
    preguntas = [
        "¿Cuántos días de teletrabajo se permiten y qué requisitos tiene?",
        "¿Qué pasos hay que seguir para solicitar formación y quién lo gestiona?",
        "¿Qué políticas afectan a un empleado que pide vacaciones y teletrabajo a la vez?",
    ]
    for q in preguntas:
        print(f"\nQ: {q}")
        respuesta = rag.search(query_text=q, retriever_config={"top_k": 4})
        print(f"A: {respuesta.answer}")

    driver.close()
