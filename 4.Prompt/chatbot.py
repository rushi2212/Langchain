# Chatbot using LangChain init_chat_model with Google Gemini

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

# Initialize Gemini Flash via LangChain's unified init
# Requires GOOGLE_API_KEY to be set in your environment or .env file
model = init_chat_model("google_genai:gemini-2.0-flash")

print("Chatbot (type 'exit' to quit):")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Exiting the chatbot. Goodbye!")
        break
    result = model.invoke(user_input)
    # result is an AIMessage; use .content for text
    print("Bot:", result.content)


# Chatbot using Langchain and OpenAI (Not Free)

# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatOpenAI()

# while True:
#     user_input = input("You: ")
#     if user_input =='exit':
#         print("Exiting the chatbot. Goodbye!")
#         break
#     result = model.invoke(user_input)
#     print("Bot:", result.content)


# Chatbot using Langchain and Local Model (FLAN-T5 Large) Working but not proper and slow
# from langchain_huggingface import HuggingFacePipeline
# from transformers import pipeline

# # Load locally
# generator = pipeline("text2text-generation", model="google/flan-t5-large")

# llm = HuggingFacePipeline(pipeline=generator)

# print("Chatbot (type 'exit' to quit):")
# while True:
#     user_input = input("You: ")
#     if user_input.lower() == "exit":
#         print("Exiting the chatbot. Goodbye!")
#         break
#     response = llm.invoke(user_input)
#     print("Bot:", response)


# ## Chatbot using Langchain and OpenAI (Not Free) with chat history

# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv

# load_dotenv()

# model = ChatOpenAI()
# chat_history = []

# while True:
#     user_input = input("You: ")
#     chat_history.append(user_input)
#     if user_input =='exit':
#         print("Exiting the chatbot. Goodbye!")
#         break
#     result = model.invoke(chat_history)
#     chat_history.append(result.content)
#     print("Bot:", result.content)

# print("Chat history:", chat_history)


# Chatbot using Langchain and Google Gemini
# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv

# load_dotenv()

# Initialize Gemini model (make sure GOOGLE_API_KEY is in your .env)
# model = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# chat_history = []

# while True:
#     user_input = input("You: ")
#     if user_input.lower() == "exit":
#         print("Exiting the chatbot. Goodbye!")
#         break

#     # Add user message
#     chat_history.append({"role": "user", "content": user_input})

#     # Convert chat history into prompt
#     prompt = "\n".join([f"{m['role'].capitalize()}: {m['content']}" for m in chat_history])

#     # Get model response
#     result = model.invoke(prompt)

#     # Add bot reply to history
#     chat_history.append({"role": "assistant", "content": result.content})

#     print("Bot:", result.content)

# print("Chat history:", chat_history)
