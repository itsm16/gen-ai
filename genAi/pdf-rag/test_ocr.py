from pathlib import Path

from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption
from langchain_docling.loader import DoclingLoader

pdf_path = Path(__file__).parent / "nodejs.pdf"

pipeline_options = PdfPipelineOptions(
    do_ocr=True,
    images_scale=1.0,
)

loader = DoclingLoader(
    file_path=pdf_path,
    converter=DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options),
        }
    ),
    convert_kwargs={"page_range": (1, 1)},
)

docs = loader.load()

for doc in docs:
    print(doc.page_content)
