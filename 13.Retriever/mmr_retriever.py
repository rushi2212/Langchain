from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document

# Sample documents
docs = [
    Document(page_content="Langchain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database that helps you store and search through embeddings."),
    Document(page_content="Pinecone is a vector database that helps you store and search through embeddings."),
    Document(page_content="OpenAI provides powerful embedding models.")
]

# Initialize embeddings
embedding_model = HuggingFaceEmbeddings()

# Create FAISS vector store
vectorstore = FAISS.from_documents(docs, embedding_model)

# Enable MMR in retriever
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 3, "lambda_mult": 0}
)

# Query
query = "What is langchain?"
results = retriever.invoke(query)

# Print results
for i, doc in enumerate(results):
    print(f"\n--Result {i+1} ---")
    print(doc.page_content)