from langchain_community.document_loaders import TextLoader
#from langchain_openai import OpenAI
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

prompt = PromptTemplate(
    template="Summarize the following text:\n\n{context}",
    input_variables=["context"]
)

parser = StrOutputParser()

loader = TextLoader("C:\\Users\\rushi\\OneDrive\\Documents\\AI\\Langchain_models\\10.DocumentLoaders\\example.txt", encoding="utf8")
documents = loader.load()
# print(documents)
# print(len(documents))
# print(type(documents))
# print(documents[0])

chain = prompt | model | parser
result = chain.invoke({"context": documents[0].page_content})
print(result)
