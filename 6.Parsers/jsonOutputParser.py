from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",  # a model available on HF Inference API
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template="Give me the name, age and city of a person \n {format_instructions}",
    input_variables=[],
    partial_variables={'format_instructions': parser.get_format_instructions()},
)

# prompt = template.format()
# result = model.invoke(prompt)
# final_result = parser.parse(result.content)
# print("Prompt:\n", prompt)
# print("Final Result:\n", final_result)
# print(final_result['name'])  # Accessing specific fields
# print(type(final_result))  # dict

chain = template | model | parser
result = chain.invoke({})
print("Final Result:\n", result)