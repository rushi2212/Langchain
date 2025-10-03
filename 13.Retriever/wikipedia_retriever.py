# Install required packages
#!pip install langchain chromadb faiss-cpu openai tiktoken langchain_openai langchain_community wikipedia

from langchain_community.retrievers import WikipediaRetriever

# Initialize the retriever
retriever = WikipediaRetriever(language="en", top_k_results=2)

# Define the query
query = "the geopolitical history of India and Pakistan from the perspective of a Chinese"

# Retrieve relevant Wikipedia documents
docs = retriever.invoke(query)

# Print retrieved content
for i, doc in enumerate(docs):
    print(f"Document {i + 1}:")
    print(f"Content:\n{doc.page_content}")
    print("\n---\n")