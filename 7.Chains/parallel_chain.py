from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
from langchain_groq import ChatGroq
import os

load_dotenv()

model1 = init_chat_model("google_genai:gemini-2.0-flash")
model2 = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

prompt1 = PromptTemplate(
    input_variables=["text"],
    template="Generate short and simple notes from the following text: {text}.",
)

prompt2 = PromptTemplate(
    input_variables=["text"],
    template="Generate 5 short question answers from the following text \n: {text}.",
)

prompt3 = PromptTemplate(
    input_variables=["notes", "quiz"],
    template="Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}.",
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    "notes": prompt1 | model1 | parser,
    "quiz": prompt2 | model2 | parser,
})

merge_chain = prompt3 | model1 | parser
chain = parallel_chain | merge_chain

text = """Artificial Intelligence (AI) is a branch of computer science that aims to create machines capable of intelligent behavior. It encompasses various subfields, including machine learning, natural language processing, computer vision, and robotics. AI systems can analyze data, recognize patterns, and make decisions with minimal human intervention. Applications of AI are widespread, ranging from virtual assistants and recommendation systems to autonomous vehicles and medical diagnostics. As AI technology continues to advance, it holds the potential to revolutionize industries and improve various aspects of daily life.AI also raises ethical considerations, such as data privacy, job displacement, and the need for transparent decision-making processes. Ongoing research and development in AI strive to address these challenges while maximizing the benefits of intelligent systems.AI is a rapidly evolving field that promises to shape the future of technology and society."""

response = chain.invoke({text})
print(response)

chain.get_graph().print_ascii()
