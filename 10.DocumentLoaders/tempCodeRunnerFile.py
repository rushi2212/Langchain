from langchain_community.document_loaders import WebBaseLoader
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
    template="Answer the following question:\n{question} from the following text -\n {text}",
    input_variables=['question','text']
)

parser = StrOutputParser()

url = "https://en.wikipedia.org/wiki/Artificial_intelligence"

loader = WebBaseLoader(url)
data = loader.load()    
# print(len(data))
# print(data[0].page_content) 

chain = prompt | model | parser

result = chain.invoke({'question' : 'What is the history og AI ?', 'text':data[0].page_content})

print(result)