#from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnablePassthrough, RunnableLambda, RunnableParallel , RunnableBranch 
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template="Write a detailed report on {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Write a short summary of the following report: {report}",
    input_variables=["report"]
)

model = ChatGroq(
    model="llama-3.3-70b-versatile",    
    api_key=os.getenv("GROQ_API_KEY")
)

parser = StrOutputParser()

#report_gen_chain = RunnableSequence(prompt1, model, parser)
report_gen_chain = prompt1 | model | parser

branch_chain = RunnableBranch(  
    (lambda x: len(x.split()) > 500, prompt2 | model | parser),
    RunnablePassthrough()
)

final_chain = RunnableSequence(
    report_gen_chain,
    branch_chain
)

print(final_chain.invoke({"topic": "Russia Ukraine war"}))
