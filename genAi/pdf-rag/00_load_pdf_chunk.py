# LOAD PDF AND CHUNK

import os
from pathlib import Path

from dotenv import load_dotenv
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption
from langchain_docling.loader import DoclingLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from google import genai

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise SystemExit("GOOGLE_API_KEY not found in .env file")

client = genai.Client(api_key=GOOGLE_API_KEY)

pdf_path = Path(__file__).parent / "nodejs.pdf"

converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(
            pipeline_options=PdfPipelineOptions(
                do_ocr=False,
                images_scale=0.5,
            ),
        ),
    },
)

# Load pdf
loader = DoclingLoader(
    file_path=pdf_path,
    converter=converter,
    convert_kwargs={"page_range": (2, 6)},
)

docs = loader.load()

for doc in docs:
    print(doc.page_content)
    print("---")

# chunk
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=400
)

chunks=text_splitter.split_documents(documents=docs)

result = client.models.embed_content(
    model="gemini-embedding-2",
    contents="contents"
)