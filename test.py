from rag.retriever import SchemaRetriever
from rag.self_rag_critic import SelfRAGCritic

retriever = SchemaRetriever()
critic = SelfRAGCritic()

query = "who are the top selling artists"
chunks = retriever.retrieve(query)

result = critic.check(query, chunks)
print("Relevant enough?", result)