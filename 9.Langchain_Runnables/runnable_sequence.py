#from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence   
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

prompt = PromptTemplate(
    template="Write a joke about {topic}",
    input_variables=["topic"]
)

#model = ChatOpenAI()
model = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template="Explain the following joke: {joke}",
    input_variables=["joke"]
)

chain = RunnableSequence(prompt, model, parser, prompt2, model, parser)

print(chain.invoke({"topic": "AI"}))
