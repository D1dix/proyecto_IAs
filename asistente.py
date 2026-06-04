# --- Sistema RAG base (Vector RAG con ChromaDB) ---
langchain>=0.3.0
langchain-openai>=0.2.0
langchain-community>=0.3.0
langchain-chroma>=0.1.4
langchain-text-splitters>=0.3.0
chromadb>=0.5.0
python-dotenv>=1.0.0

# --- Bonificación: GraphRAG con Neo4j ---
neo4j>=5.20
neo4j-graphrag[openai]>=1.16.0

# --- Bonificación: interfaz web ---
gradio>=4.0.0
