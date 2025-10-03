### Chatbot using Langchain and OpenAI (Not Free)
# from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatOpenAI()

# messages = [
#     SystemMessage(content="You are a helpful assistant."),
#     HumanMessage(content="Tell me about Langchain."),
# ]

# result = model.invoke(messages)
# messages.append(AIMessage(content=result.content))
# print(messages)



from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize Gemini model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=GOOGLE_API_KEY)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Tell me about LangChain."),
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)
