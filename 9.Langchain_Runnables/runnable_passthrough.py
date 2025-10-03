#from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence , RunnablePassthrough ,RunnableParallel
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
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

joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'explanation' : RunnableSequence(prompt2, model, parser)
})

final_chain = RunnableSequence(
    joke_gen_chain,
    parallel_chain
)

print(final_chain.invoke({"topic": "cricket"}))
