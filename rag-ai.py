import os
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings  # Updated name
)
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Set API Key
os.environ["GOOGLE_API_KEY"] = "AIzaSyA7e3kHqlBC6Liec9wRunVhlkL-OJEGJNQ"  # Replace with your key

# 1. Prepare Documents (create sample.txt first)
# sample_text = """Paris is the capital of France. 
# The Eiffel Tower is the most iconic landmark in Paris.
# The Louvre Museum houses the Mona Lisa.
# The Seine River flows through the city."""

# with open("sample.txt", "w") as f:
#     f.write(sample_text)

# 2. Load and Split Documents
loader = TextLoader("sample.txt")
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)
splits = text_splitter.split_documents(docs)

# 3. Create Vector Store
embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
vectorstore = FAISS.from_documents(
    documents=splits,
    embedding=embedding
)

# 4. Create Retriever
retriever = vectorstore.as_retriever()

# 5. Create RAG Chain
template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0)

rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()} 
    | prompt 
    | model 
    | StrOutputParser()
)

# 6. Ask a Question
question = "What is the most iconic landmark in Paris?"
response = rag_chain.invoke(question)
print(response)