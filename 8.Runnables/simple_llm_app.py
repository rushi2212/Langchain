from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

#Initialize the LLM
llm = OpenAI(model_name="text-davinci-003", temperature=0.7)

# Create a simple prompt template
prompt = PromptTemplate(
    input_variables=["question"],
    template="What is the answer to the following question? {question}"
)

# Define the input
question = input("Enter a question: ")

# Generate the prompt
formatted_prompt = prompt.format(question=question)

# Get the response from the LLM
response = llm(formatted_prompt)

# Print the response
print("LLM Response:", response)