# from langchain.schema.runnable import RunnableLambda

# def word_counter(text):
#     return len(text.split())

# word_count_chain = RunnableLambda(word_counter)
# print(word_count_chain.invoke("Hello, how are you doing today?"))


#from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnablePassthrough, RunnableLambda, RunnableParallel   
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

def word_counter(text):
    return len(text.split())

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

joke_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'word_count' : RunnableLambda(word_counter)
})

final_chain = RunnableSequence(
    joke_gen_chain,
    parallel_chain
)

print(final_chain.invoke({"topic": "cricket"})) 
