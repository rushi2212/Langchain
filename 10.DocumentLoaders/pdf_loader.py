from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("C:\\Users\\rushi\\OneDrive\\Documents\\AI\\Langchain_models\\10.DocumentLoaders\\example.pdf")
documents = loader.load()
print(documents)
print(len(documents))

print(documents[0].page_content)
print(documents[0].metadata)