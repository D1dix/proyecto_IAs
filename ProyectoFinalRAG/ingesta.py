"""
Ingesta GraphRAG: construye un grafo de conocimiento en Neo4j a partir de los
MISMOS documentos del Vector RAG base (extra/bonificación de la sesión 3).

El SimpleKGPipeline se encarga de: chunking + extracción de entidades y
relaciones con un LLM + escritura del grafo en Neo4j. Después se crea un índice
vectorial sobre los chunks para poder usar el VectorCypherRetriever.

Uso:
    python ingesta_graphrag.py

Requiere en .env: OPENAI_API_KEY, NEO4J_URI, NEO4J_USERNAME, NEO4J_PASSWORD.
"""

import os
import asyncio
from pathlib import Path
from dotenv import load_dotenv

import neo4j
from neo4j_graphrag.embeddings import OpenAIEmbeddings
from neo4j_graphrag.llm import OpenAILLM
from neo4j_graphrag.experimental.pipeline.kg_builder import SimpleKGPipeline

load_dotenv()

# --- Esquema sugerido para los documentos de TechCorp ---
# Si se omite, el LLM infiere entidades libremente (menos control, más ruido).
ENTITIES = [
    {"label": "Politica", "description": "Política interna de la empresa"},
    {"label": "Procedimiento", "description": "Procedimiento operativo"},
    {"label": "Departamento", "description": "Departamento o área (RRHH, IT, Soporte...)"},
    {"label": "Recurso", "description": "Recurso, herramienta o sistema mencionado"},
    {"label": "Plazo", "description": "Plazo, antelación o duración temporal"},
]
RELATIONS = [
    {"label": "APLICA_A", "description": "Una política aplica a un departamento o recurso"},
    {"label": "REQUIERE", "description": "Un procedimiento requiere un recurso o plazo"},
    {"label": "GESTIONADO_POR", "description": "Un proceso gestionado por un departamento"},
]
POTENTIAL_SCHEMA = [
    ("Politica", "APLICA_A", "Departamento"),
    ("Politica", "APLICA_A", "Recurso"),
    ("Procedimiento", "REQUIERE", "Recurso"),
    ("Procedimiento", "REQUIERE", "Plazo"),
    ("Procedimiento", "GESTIONADO_POR", "Departamento"),
]


async def main() -> None:
    driver = neo4j.GraphDatabase.driver(
        os.environ["NEO4J_URI"],
        auth=(os.environ["NEO4J_USERNAME"], os.environ["NEO4J_PASSWORD"]),
    )

    # La extracción de entidades devuelve JSON -> activamos json_object.
    llm = OpenAILLM(
        model_name="gpt-4o-mini",
        model_params={"temperature": 0, "response_format": {"type": "json_object"}},
    )
    embedder = OpenAIEmbeddings(model="text-embedding-3-small")

    kg_builder = SimpleKGPipeline(
        driver=driver,
        llm=llm,
        embedder=embedder,
        entities=ENTITIES,
        relations=RELATIONS,
        potential_schema=POTENTIAL_SCHEMA,
        from_pdf=False,                  # pasamos texto plano
        perform_entity_resolution=True,  # fusiona entidades equivalentes
    )

    docs_dir = Path("./documentos")
    for txt_path in docs_dir.glob("*.txt"):
        print(f"Procesando {txt_path.name}...")
        await kg_builder.run_async(text=txt_path.read_text(encoding="utf-8"))

    # Índice vectorial sobre los chunks (1536 dims = text-embedding-3-small)
    with driver.session() as session:
        session.run("""
            CREATE VECTOR INDEX chunk_embeddings IF NOT EXISTS
            FOR (c:Chunk) ON (c.embedding)
            OPTIONS { indexConfig: {
                `vector.dimensions`: 1536,
                `vector.similarity_function`: 'cosine'
            }}
        """)

    driver.close()
    print("Grafo construido. Abre Neo4j Browser y ejecuta: MATCH (n) RETURN n LIMIT 50;")


if __name__ == "__main__":
    asyncio.run(main())
