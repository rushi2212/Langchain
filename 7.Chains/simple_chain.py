from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Generate 5 intresting facts about {topic}.",
)

model = init_chat_model("google_genai:gemini-2.0-flash")

parser = StrOutputParser()

chain = prompt | model | parser
response = chain.invoke({"topic": "cricket"})
print(response) 

chain.get_graph().print_ascii()