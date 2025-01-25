from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize the Gemini Pro model
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", temperature = 0.3)

# Ask your question
question = "Tell me a joke"
response = model.invoke(question)

# Print the response
print(response.content)