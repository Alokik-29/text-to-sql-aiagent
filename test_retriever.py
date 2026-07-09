from rag.retriever import SchemaRetriever

retriever = SchemaRetriever()
results = retriever.retrieve("who are the top selling artists")
for r in results:
    print(r["table"])
    print(r["text"])
    print("---")