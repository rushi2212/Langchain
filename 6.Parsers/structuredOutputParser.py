from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",  # a model available on HF Inference API
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

schema = [
    ResponseSchema(name="fact_1", description="Fact 1 about the topic"),
    ResponseSchema(name="fact_2", description="Fact 2 about the topic"),
    ResponseSchema(name="fact_3", description="Fact 3 about the topic"),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Give me three facts about the topic: {topic}\n{format_instructions}",
    input_variables=["topic"],
    partial_variables={'format_instructions': parser.get_format_instructions()},
)

# prompt = template.invoke({"topic": "Machine Learning"})
# result = model.invoke(prompt)

# output = parser.parse(result.content)
# print(output)

chain = template | model | parser
response = chain.invoke({"topic": "Machine Learning"})
print(response)