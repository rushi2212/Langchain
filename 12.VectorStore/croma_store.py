# -*- coding: utf-8 -*-

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.schema import Document
from langchain_chroma import Chroma


# 1️⃣ Initialize embeddings
embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# 2️⃣ Create sample documents
doc1 = Document(
    page_content="Rohit’s performance with MI has been significant: he has contributed heavily with the bat, including scoring centuries for MI in the IPL. Over time, he became a symbolic figure for the franchise — his leadership, batting exploits, and consistency made him one of the faces of MI.",
    metadata={"team": "mumbai indians"}
)

doc2 = Document(
    page_content="Kohli is one of the most prolific run-scorers in modern cricket and widely regarded as one of the best batsmen of his generation. In ODIs, he holds the record for the most centuries by an Indian.",
    metadata={"team": "royal challengers bangalore"}
)

doc3 = Document(
    page_content="One of the first players in the IPL (2008), bought by Chennai Super Kings (CSK). He has captained CSK for many seasons (2008-2023, except when the team was suspended in 2016-17). Titles: under Dhoni, CSK have won the IPL several times — 2010, 2011, 2018, 2021, 2023.",
    metadata={"team": "chennai super kings"}
)

# 3️⃣ Initialize Chroma vector store
vector_store = Chroma(
    embedding_function=embedding_function,
    persist_directory='chroma_db',
    collection_name="sample"
)

# 4️⃣ Add documents to the vector store
docs = [doc1, doc2, doc3]
vector_store.add_documents(docs)

# 5️⃣ View all documents in the store
vector_store.get(include=['embeddings', 'documents', 'metadatas'])

# 6️⃣ Perform similarity search
vector_store.similarity_search(query="who is csk player", k=1)
vector_store.similarity_search_with_score(query="who is MI player", k=1)

# 7️⃣ Filter-based similarity search
vector_store.similarity_search_with_score(query="", filter={"team": "mumbai indians"})

# 8️⃣ Update a document
updated_doc1 = Document(
    page_content="Rohit is best cricketer. Rohit’s performance with MI has been significant: he has contributed heavily with the bat, including scoring centuries for MI in the IPL. Over time, he became a symbolic figure for the franchise — his leadership, batting exploits, and consistency made him one of the faces of MI. Rohit Sharma is Indian Player.",
    metadata={"team": "mumbai indians"}
)
vector_store.update_document(document_id='f1c47a75-2c60-4a5f-8a4d-1d69e7fd83a9', document=updated_doc1)

# 9️⃣ Delete a document
vector_store.delete(ids=['60636717-6d88-48ea-9956-b0626b20201f'])

# 10️⃣ View documents after deletion
vector_store.get(include=['embeddings', 'documents', 'metadatas'])
