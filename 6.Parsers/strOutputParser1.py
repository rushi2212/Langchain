###Using OpenAI with Langchain
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


model = init_chat_model("google_genai:gemini-2.0-flash")

# 1st prompt -> detailed report
template1 = PromptTemplate( 
    
    template="Write a detailed report on the following topic: {topic}",
    input_variables=["topic"]
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    
    template="Summarize the following topic in 5 lines: {topic}",
    input_variables=["topic"]
)


parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({"topic": "Black holes"})
print(result)
