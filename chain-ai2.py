from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyA7e3kHqlBC6Liec9wRunVhlkL-OJEGJNQ"

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", temperature=0.7)

# Chain 1: Generate joke
joke_prompt = ChatPromptTemplate.from_template(
    "Tell me a {style} joke about {topic}"
)
joke_chain = joke_prompt | model | StrOutputParser()

# Chain 2: Explain joke
explain_prompt = ChatPromptTemplate.from_template(
    "Explain why this joke is funny: {joke}"
)
explain_chain = explain_prompt | model | StrOutputParser()

# Combine both chains
full_chain = {"joke": joke_chain} | explain_chain

# Invoke with parameters
result = full_chain.invoke({
    "style": "science-themed",
    "topic": "planets"
})

print(result)