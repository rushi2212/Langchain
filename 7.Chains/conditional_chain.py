from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain.schema.runnable import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = init_chat_model("google_genai:gemini-2.0-flash")

# Parser for classification
class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(
        description="Give sentiment of the feedback."
    )

parser = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=Feedback)

# --- Step 1: Classifier ---
prompt1 = PromptTemplate(
    input_variables=["feedback"],
    template=(
        "Classify the sentiment of the following feedback into positive or negative.\n"
        "Feedback: {feedback}\n"
        "{format_instructions}"
    ),
    partial_variables={"format_instructions": parser2.get_format_instructions()},
)

classifier_chain = prompt1 | model | parser2

# --- Step 2: Positive branch ---
prompt2 = PromptTemplate(
    input_variables=["feedback"],
    template="Write an appropriate response to this positive feedback: {feedback}.",
)

# --- Step 3: Negative branch ---
prompt3 = PromptTemplate(
    input_variables=["feedback"],
    template="Write an appropriate response to this negative feedback: {feedback}.",
)

# --- Step 4: Branch logic ---
branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", prompt2 | model | parser),
    (lambda x: x.sentiment == "negative", prompt3 | model | parser),
    RunnableLambda(lambda x: "No sentiment detected."),
)

# Combine chains
chain = classifier_chain | branch_chain

response = chain.invoke({"feedback": "The smartphone is wonderful."})
print(response)

chain.get_graph().print_ascii()
