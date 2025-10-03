#from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence , RunnableParallel 
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate a tweet about {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Generate a linkedin post about {topic}",
    input_variables=["topic"]
)

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet' : RunnableSequence(prompt1, model, parser),
    'linkedin_post' : RunnableSequence(prompt2, model, parser)
})

results = parallel_chain.invoke({"topic": "AI"})
print(results)
print("\n \n")
print("Tweet:", results['tweet'])
print("\n \n")
print("LinkedIn Post:", results['linkedin_post'])