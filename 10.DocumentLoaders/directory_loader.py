from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(path='Langchain_models\\10.DocumentLoaders\\Notes', glob="*.pdf", loader_cls=PyPDFLoader)

documents = loader.lazy_load()

# print(len(documents))
# print(documents[90].page_content)
# print(documents[90].metadata)

for doc in documents:
    print(doc.metadata)
    