# from langchain_openai import OpenAIEmbeddings
# from dotenv import load_dotenv
# from sklearn.metrics.pairwise import cosine_similarity
# import numpy as np

# # Load environment variables (make sure OPENAI_API_KEY is in your .env)
# load_dotenv()

# # Initialize embeddings (dim=32 to reduce vector size for demo)
# embeddings = OpenAIEmbeddings(
#     model="text-embedding-3-large",
#     dimensions=32
# )

# # List of documents
# documents = [
#     "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
#     "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
#     "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
#     "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
#     "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
# ]

# query = "Tell me about virat kohli"

# doc_embeddings = embeddings.embed_documents(documents)
# query_embedding = embeddings.embed_query(query)

# cosine_similarities = cosine_similarity([query_embedding], doc_embeddings)[0]

# index, score = sorted(list(enumerate(cosine_similarities)), key=lambda x: x[1])[-1]

# print(query)
# print(documents[index])
# print("Similarity Score: ", score)


from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

# Use free HuggingFace embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# List of documents
documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = "Tell me about bumrah"

# Generate embeddings
doc_embeddings = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)

# Cosine similarity
cosine_similarities = cosine_similarity([query_embedding], doc_embeddings)[0]

# Find best match
index, score = sorted(list(enumerate(cosine_similarities)), key=lambda x: x[1])[-1]

print(query)
print("Matched Document:", documents[index])
print("Similarity Score:", score)
