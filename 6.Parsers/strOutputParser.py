
#import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

# HF_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",  # a model available on HF Inference API
    task="text-generation",
    # huggingfacehub_api_token=HF_TOKEN
)
model = ChatHuggingFace(llm=llm)

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

prompt1 = template1.invoke({"topic": "Artificial Intelligence"})
result = model.invoke(prompt1)

prompt2 = template2.invoke({"topic": result.content})
result1 = model.invoke(prompt2)

print("Detailed Report:\n", result.content)
print("\nSummary:\n", result1.content)




###Using OpenAI with Langchain###
# from langchain.chat_models import init_chat_model
# from dotenv import load_dotenv
# from langchain_core.prompts import PromptTemplate

# load_dotenv()


# model = init_chat_model("google_genai:gemini-2.0-flash")

# # 1st prompt -> detailed report
# template1 = PromptTemplate( 
    
#     template="Write a detailed report on the following topic: {topic}",
#     input_variables=["topic"]
# )

# # 2nd prompt -> summary
# template2 = PromptTemplate(
    
#     template="Summarize the following topic in 5 lines: {topic}",
#     input_variables=["topic"]
# )

# prompt1 = template1.invoke({"topic": "Artificial Intelligence"})
# result = model.invoke(prompt1)

# prompt2 = template2.invoke({"topic": result.content})
# result1 = model.invoke(prompt2)

# print("Detailed Report:\n", result.content)
# print("\nSummary:\n", result1.content)
