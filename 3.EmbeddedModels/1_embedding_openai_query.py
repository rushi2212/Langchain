#Not Free
# from langchain_openai import OpenAIEmbeddings
# from dotenv import load_dotenv

# load_dotenv()

# embeddings = OpenAIEmbeddings(
#     model="text-embedding-3-small",
#     dimensions=32   # ✅ correct parameter
# )

# result = embeddings.embed_query("Delhi is the capital of India")
# print(result)




#pip install sentence-transformers

from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

result = embeddings.embed_query("Delhi is the capital of India")
print(len(result), result[:10])  # vector length + preview
