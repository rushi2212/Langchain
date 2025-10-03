### Giving error
# from langchain_openai import ChatOpenAI

# from dotenv import load_dotenv
# import streamlit as st
# load_dotenv()

# st.header("Research Tool")

# paper_input = st.selectbox("Enter the research paper Name", ["Attentions Is All You Need","BERT: Pro-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Larners", "Diffusion Model Beat GANs on Image Synthesis"])

# style_input = st.selectbox("Select Explanation Style", ["Beginner-friendly", "Technical", "Code-Oriented", "Mathematical"])

# length_input = st.selectbox("Select Explanation Length", ["Short (1-2 paragraphs)","Medium (3-5 paragraphs)", "Long (detailed explanation)"])

# # template
# template = PromptTemplate(
#     template = """
# Please summarize the research paper titled.

# Specifications:
# Explanation Style: {style_input}
# Explanation Length: {length_input}

# 1. Mathematical Details:
# "{paper_input}"
# Include relevant mathematical equations if present in the paper.
# Explain the mathematical concepts using simple, intuitive code snippets where applicable.

# 2. Analogies:
# Use relatable analogies to simplify complex ideas.

# If certain information is not available in the paper, respond with:
# "Insufficient information available" instead of guessing.

# Ensure the summary is clear, accurate, and aligned with the provided style and length.
# """,
# input_variables=["paper_input", "style_input", "length_input"]
# )

# #fill the placeholders
# prompt = template.invoke({paper_input: paper_input, style_input: style_input, length_input: length_input})

# if st.button('Summarize'):
#     result = model.invoke(user_input)
#     st.write(result.content)


### Not Free
# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv
# import streamlit as st
# import os

# # Load .env variables
# load_dotenv()

# # Initialize OpenAI model
# model = ChatOpenAI(
#     openai_api_key=os.getenv("OPENAI_API_KEY"),  # Make sure this is in your .env
#     model="gpt-3.5-turbo"  # or "gpt-4o-mini" etc.
# )

# st.header("Research Tool")

# user_input = st.text_input("Enter your query here")

# if st.button('Summarize'):
#     if user_input.strip():
#         result = model.invoke(user_input)
#         st.write(result.content)
#     else:
#         st.warning("Please enter a query first.")


### Free
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import streamlit as st
import os
from langchain_core.prompts import PromptTemplate, load_prompt

# Load .env variables (make sure you have HUGGINGFACEHUB_API_TOKEN in .env)
load_dotenv()

# Initialize Hugging Face LLM
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",  # change model if you want
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

model = ChatHuggingFace(llm=llm)

# Streamlit UI
st.header("Research Tool - Hugging Face")

paper_input = st.selectbox("Enter the research paper Name", ["Attentions Is All You Need","BERT: Pro-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Larners", "Diffusion Model Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select Explanation Style", ["Beginner-friendly", "Technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select Explanation Length", ["Short (1-2 paragraphs)","Medium (3-5 paragraphs)", "Long (detailed explanation)"])

template = load_prompt('template.json')

#Or
# template
# template = PromptTemplate(
#     template = """
# Please summarize the research paper titled.

# Specifications:
# Explanation Style: {style_input}
# Explanation Length: {length_input}

# 1. Mathematical Details:
# "{paper_input}"
# Include relevant mathematical equations if present in the paper.
# Explain the mathematical concepts using simple, intuitive code snippets where applicable.

# 2. Analogies:
# Use relatable analogies to simplify complex ideas.

# If certain information is not available in the paper, respond with:
# "Insufficient information available" instead of guessing.

# Ensure the summary is clear, accurate, and aligned with the provided style and length.
# """,
# input_variables=["paper_input", "style_input", "length_input"]
# )

#fill the placeholders
# fill the placeholders correctly
# prompt = template.invoke({
#     "paper_input": paper_input,
#     "style_input": style_input,
#     "length_input": length_input
# })

if st.button('Summarize'):
    #chain
    chain = template | model
    summary = chain.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input
    })
    st.write(summary.content)
