# LOAD PDF => CHUNK => QDRANT

import os
from pathlib import Path

from dotenv import load_dotenv
from pypdf import PdfReader

from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption
from langchain_docling.loader import DoclingLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_qdrant import QdrantVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise SystemExit("GOOGLE_API_KEY not found in .env file")

QDRANT_URL = os.getenv("QDRANT_URL", "http://localhost:6333")
COLLECTION_NAME = "nodejs_pdf"
BATCH_SIZE = 10
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
EMBED_BATCH_SIZE = 20


def index() -> QdrantVectorStore:
    pdf_path = Path(__file__).parent / "nodejs.pdf"
    total_pages = len(PdfReader(pdf_path).pages)
    print(f"PDF has {total_pages} pages")

    pipeline_options = PdfPipelineOptions(
        do_ocr=False,
        images_scale=0.5,
    )
    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options),
        },
    )

    all_docs = []
    for start in range(1, total_pages + 1, BATCH_SIZE):
        end = min(start + BATCH_SIZE - 1, total_pages)
        print(f"Processing pages {start}–{end} ...")
        loader = DoclingLoader(
            file_path=pdf_path,
            converter=converter,
            convert_kwargs={"page_range": (start, end)},
        )
        all_docs.extend(loader.load())
        print(f"  -> {len(all_docs)} docs so far")

    print(f"Total docs extracted: {len(all_docs)}")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
    )
    chunks = text_splitter.split_documents(all_docs)
    print(f"Split into {len(chunks)} chunks")

    embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2")

    print("Embedding chunks and storing in Qdrant ...")
    vector_store = QdrantVectorStore.from_documents(
        documents=chunks,
        embedding=embeddings,
        url=QDRANT_URL,
        collection_name=COLLECTION_NAME,
        prefer_grpc=False,
        batch_size=EMBED_BATCH_SIZE,
    )

    print(f"Successfully indexed {len(chunks)} chunks into Qdrant collection '{COLLECTION_NAME}'")
    return vector_store


if __name__ == "__main__":
    index()
