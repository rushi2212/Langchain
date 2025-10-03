from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    input_variables=["topic"],
    template="Generate a detailed report on {topic}.",
)

prompt2 = PromptTemplate(   
    input_variables=["text"],
    template="Generate a 5 pointer summary from the following text \n: {text}.",
)

model = init_chat_model("google_genai:gemini-2.0-flash")

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser
response = chain.invoke({"topic": "unemployment in India"})
print(response) 

chain.get_graph().print_ascii()