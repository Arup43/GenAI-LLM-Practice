import os
from langchain_google_genai import ChatGoogleGenerativeAI

# Set your Google API key (get it from https://makersuite.google.com/app/apikey)
os.environ["GOOGLE_API_KEY"] = "AIzaSyA7e3kHqlBC6Liec9wRunVhlkL-OJEGJNQ"  # Replace with your actual API key

# Initialize the Gemini Pro model
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", temperature = 0.3)

# Ask your question
question = "Tell me a joke"
response = model.invoke(question)

# Print the response
print(response.content)