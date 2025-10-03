from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",  # a model available on HF Inference API
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

class Person(BaseModel):
    name: str = Field(description="The person's full name")
    age: int = Field(gt=18, description="The person's age in years")
    city: str = Field(description="The city where the person lives")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Generate a random person with name, age, and city of a fictional {place} person \n{format_instructions}",
    input_variables=['place'],
    partial_variables={'format_instructions': parser.get_format_instructions()},
)

# prompt = template.invoke({"place": "Indian"})
# print(prompt)
# result = model.invoke(prompt)
# output = parser.parse(result.content)
# print(output)

chain = template | model | parser
response = chain.invoke({"place": "japanese"})
print(response)