from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="Langchain_models/10.DocumentLoaders/example.csv", encoding="utf8")
docs = loader.load()
print(len(docs))
print(docs[0])