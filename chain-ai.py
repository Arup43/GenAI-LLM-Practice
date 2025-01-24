from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
import os

os.environ["GOOGLE_API_KEY"] = "AIzaSyA7e3kHqlBC6Liec9wRunVhlkL-OJEGJNQ" 

# 1. Create components
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", temperature=0.7)
prompt = PromptTemplate.from_template(
    "Tell me a joke about {topic}. Make it funny but appropriate for kids."
)

# 2. Create chain using pipe operator (|)
chain = prompt | model | StrOutputParser()

# 3. Invoke the chain
result = chain.invoke({"topic": "robots"})
print(result)