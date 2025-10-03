# Not Free
# from langchain_openai import OpenAIEmbeddings
# from dotenv import load_dotenv

# load_dotenv()

# embeddings = OpenAIEmbeddings(
#     model="text-embedding-3-small",
#     dimensions=32   # ✅ correct parameter
# )

# documents = [
#     "Delhi is the capital of India",
#     "Mumbai is the financial capital of India",
#     "Kolkata is the cultural capital of India"
# ]

# result = embeddings.embed_documents(documents)
# print(str(result))



from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

docs = [
    "Delhi is the capital of India",
    "Mumbai is the financial capital of India",
    "Kolkata is the cultural capital of India"
]

result = embeddings.embed_documents(docs)
print(result)
