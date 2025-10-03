# from langchain.text_splitter import CharacterTextSplitter

# text = """To be, or not to be, that is the question:
# Whether 'tis nobler in the mind to suffer
# The slings and arrows of outrageous fortune,
# Or to take arms against a sea of troubles
# And by opposing end them.The text continues with more lines to ensure it exceeds the max_length for splitting.Here is some additional text to make sure we have enough content to demonstrate the splitting functionality effectively."""

# splitter = CharacterTextSplitter(
#     chunk_size=100,
#     chunk_overlap=0,
#     separator=''
# )

# texts = splitter.split_text(text)
# print(texts)


from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("Langchain_models/11.TextSplitters/example.pdf")

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)

texts = splitter.split_documents(docs)
print(texts[0].page_content)
