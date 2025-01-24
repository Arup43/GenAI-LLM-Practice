import os
from langchain_google_genai import ChatGoogleGenerativeAI

# Set your Google API key (get it from https://makersuite.google.com/app/apikey)
os.environ["GOOGLE_API_KEY"] = "AIzaSyA7e3kHqlBC6Liec9wRunVhlkL-OJEGJNQ"  # Replace with your actual API key

# Initialize the Gemini Pro model
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# Ask your question
question = "What is the capital of France?"
response = model.invoke(question)

# Print the response
print(response.content)