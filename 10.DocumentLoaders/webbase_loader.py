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

url = "https://www.amazon.in/Dell-Inspiron-3535-Windows-Processor/dp/B0DG5CY2Y2/ref=sr_1_1_sspa?dib=eyJ2IjoiMSJ9.m0DifAK8mDUTDRf0Mrv_UkLdt3F7iEKg5fwmI5hGYEAwGJxKfu-BGssBB53TEeC92ddyHwTzgpuZQBAEitvSE1VYl0nlrZr8xsQJYROT7nmsSLDm3kba2IlPSsK6UyICRBsMGeSTYtsaA6Bqr7Wg5AQmGP7zVof_vIdenMvw_32vXG06e_69bMaLwHoe7B-kSoTxYa0zPCdDHnZio93yZlyak2E8DOvGSYWiKxa1z2g.T3GbIAozmt6Ra6gB6JA2YPtjXgixbiZXELeUXn7H3Wg&dib_tag=se&keywords=laptop&qid=1758880808&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"

loader = WebBaseLoader(url)
data = loader.load()    
# print(len(data))
# print(data[0].page_content) 

chain = prompt | model | parser

result = chain.invoke({'question' : 'What is the product that we are talking about ?', 'text':data[0].page_content})

print(result)