# Install required packages
#!pip install langchain chromadb langchain_community langchain_huggingface HuggingFaceEmbeddings

from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

# Step 1: Your source documents
documents = [
    Document(page_content="Langchain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database that helps you store and search through embeddings."),
    Document(page_content="Pinecone is a vector database that helps you store and search through embeddings."),
    Document(page_content="OpenAI provides powerful embedding models.")
]

# Step 2: Initialize embedding model
embedding_model = HuggingFaceEmbeddings()

# Step 3: Create Chroma vector store
vectorstore = Chroma.from_documents(
    documents,
    embedding=embedding_model,
    collection_name="my_collection"
)

# Step 4: Convert vector store into a retriever
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# Step 5: Perform semantic search
query = 'What is Chroma used for?'
results = retriever.invoke(query)

# Display results
for i, doc in enumerate(results):
    print(f"Document {i + 1}:")
    print(f"Content:\n{doc.page_content}")
    print("\n---\n")