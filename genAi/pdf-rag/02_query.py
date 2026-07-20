import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
COLLECTION_NAME = "nodejs_pdf"
MODEL = "gemini-3.1-flash-lite"

question = "crud mongodb methods with code no theory , using cli as well db.collection etc. and using mongoose"

embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2")
vector_store = QdrantVectorStore.from_existing_collection(
    collection_name=COLLECTION_NAME,
    embedding=embeddings,
    url=QDRANT_URL,
    prefer_grpc=False,
)
retriever = vector_store.as_retriever(search_kwargs={"k": 5})
docs = retriever.invoke(question)

context = "\n\n".join(d.page_content for d in docs)
prompt = (
    "Answer the question based on the provided context.\n\n, Answer in great detail when context is available for question asked"
    f"Context:\n{context}\n\n"
    f"Question: {question}\n\n"
    "Answer:"
)

client = genai.Client(api_key=GOOGLE_API_KEY)
response = client.models.generate_content(model=MODEL, contents=prompt)
print(response.text)
