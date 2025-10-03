# from langchain_experimental.text_splitter import SemanticChunker
# from langchain_openai.embeddings import OpenAIEmbeddings
# from dotenv import load_dotenv
# load_dotenv()

# # ✅ Corrected argument name
# text_splitter = SemanticChunker(
#     embeddings=OpenAIEmbeddings(),  # use 'embeddings' instead of 'embedding'
#     breakpoint_threshold_type="standard_deviation",
#     breakpoint_threshold_amount=1
# )

# sample = """
# Artificial intelligence (AI) refers to the simulation of human intelligence in machines that are programmed to think and learn like humans. These intelligent machines can perform tasks that typically require human intelligence, such as visual perception, speech recognition, decision-making, and language translation.
# Farmer John has a large collection of cows. He has N cows (1 <= N <= 100,000), each with a distinct integer ID number (1 <= ID <= 1,000,000,000). Farmer John wants to organize his cows into groups based on their ID numbers. Specifically, he wants to group cows whose ID numbers differ by at most K (0 <= K <= 1,000,000,000).
# IPL 2023 is the 16th season of the Indian Premier League (IPL), a professional Twenty20 cricket league established by the Board of Control for Cricket in India (BCCI) in 2008. The tournament features franchise teams representing different cities in India and attracts top cricketing talent from around the world.
# """

# docs = text_splitter.split_text(sample)
# print(len(docs))
# print(docs)


from langchain_experimental.text_splitter import SemanticChunker
from langchain.embeddings.huggingface import HuggingFaceEmbeddings

# Initialize embeddings
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Initialize semantic text splitter
text_splitter = SemanticChunker(
    embeddings=embeddings,  # use 'embeddings', not 'embedding'
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1
)

sample_text = """
Artificial intelligence (AI) refers to the simulation of human intelligence in machines...
Farmer John has a large collection of cows...
IPL 2023 is the 16th season of the Indian Premier League...
"""

# Split the text
chunks = text_splitter.split_text(sample_text)

print(f"Number of chunks: {len(chunks)}")
print("First chunk:", chunks[0])
