from langchain_community.document_loaders import PyPDFLoader
from pathlib import Path

pdf_path= Path(__file__).parent / "nodejs.pdf"
loader = PyPDFLoader(file_path=pdf_path)
docs= loader.load()

print(docs[12])