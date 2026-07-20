# RAG

## Stack Built So Far

| Layer | Technology | Purpose |
|-------|-----------|---------|
| Document Loader | DoclingLoader (`langchain-docling`) | AI-powered PDF parsing with layout analysis & OCR |
| Text Splitter | `RecursiveCharacterTextSplitter` | Chunk documents into overlapping segments |
| Embeddings | Google `text-embedding-004` (`langchain-google-genai`) | Convert chunks to vector embeddings |
| Vector Store | Qdrant (localhost:6333) with `langchain-qdrant` | Store & retrieve embeddings via similarity search |
| Environment | `.env` with `python-dotenv` | Securely load `GOOGLE_API_KEY` |

## Files

| File | Purpose |
|------|---------|
| `index.py` | DoclingLoader — extract PDF with OCR disabled, batch pages 2–6 |
| `main.py` | PyPDFLoader — raw text extraction (lightweight) |
| `test_ocr.py` | DoclingLoader with OCR enabled on a single page (page 1) |
| `qdrant_index.py` | Full pipeline: load PDF → Docling (batch) → chunk → embed → upsert to Qdrant. Also `--preview "<question>"` for Q&A |
| `query.py` | Standalone RAG query — connect to existing Qdrant, retrieve top-5 chunks, answer via Gemini 3.1 Flash-Lite |
| `learnings.md` | This file |

## How the RAG Pipeline Works

1. **Load** — DoclingLoader processes the PDF in batches of 10 pages to avoid OOM, with OCR enabled (`do_ocr=True`) and reduced image scale (`images_scale=0.5`)
2. **Chunk** — `RecursiveCharacterTextSplitter` splits documents into 1000-char chunks with 200-char overlap
3. **Embed** — `GoogleGenerativeAIEmbeddings` (model `text-embedding-004`) converts each chunk to a vector
4. **Index** — `QdrantVectorStore.from_documents()` creates a Qdrant collection and upserts all vectors
5. **Query** — `qdrant_index.py --preview "<question>"` or `query.py` (change `question` var) retrieves top-K chunks from Qdrant, feeds as context to Gemini 3.1 Flash-Lite (`gemini-3.1-flash-lite-001` via `google.genai` SDK), answers the question

## Key Files

### `qdrant_index.py` — Index + Preview

```python
# Indexing pipeline (batch, OCR, chunk, embed, upsert)
loader = DoclingLoader(
    file_path=pdf_path, converter=converter,
    convert_kwargs={"page_range": (start, end)},
)
chunks = text_splitter.split_documents(all_docs)
vector_store = QdrantVectorStore.from_documents(
    documents=chunks, embedding=embeddings,
    url=QDRANT_URL, collection_name=COLLECTION_NAME,
)

# Preview: retrieve top-5, answer with Gemini 3.1 Flash-Lite
def preview(query: str, vs: QdrantVectorStore) -> None:
    docs = vs.as_retriever(search_kwargs={"k": 5}).invoke(query)
    prompt = f"Answer based on context.\n\nContext:\n{...}\n\nQuestion: {query}\n\nAnswer:"
    response = client.models.generate_content(model=PREVIEW_MODEL, contents=prompt)
    print(response.text)
```

**Usage:** `python qdrant_index.py` (index only) or `python qdrant_index.py --preview "What is Node.js?"`

---

### `query.py` — Standalone Query (no re-index)

```python
question = "What is Node.js?"

embeddings = GoogleGenerativeAIEmbeddings(model="text-embedding-004")
vector_store = QdrantVectorStore.from_existing_collection(
    collection_name=COLLECTION_NAME, embedding=embeddings, url=QDRANT_URL,
)
docs = vector_store.as_retriever(search_kwargs={"k": 5}).invoke(question)
context = "\n\n".join(d.page_content for d in docs)
prompt = f"Answer based on context.\n\nContext:\n{context}\n\nQuestion: {question}\n\nAnswer:"
response = client.models.generate_content(model=MODEL, contents=prompt)
print(response.text)
```

**Usage:** `python query.py` (just change the `question` variable at the top)

---

## Docling vs PyPDFLoader

### PyPDF (used by PyPDFLoader)
- Extracts raw text from the PDF's embedded text layer only
- No layout analysis, no table detection, no OCR
- **Lightweight** — low memory, fast
- Works well for text-based PDFs (not scanned documents)
- **Not actively maintained** — development has slowed

### Docling (DoclingLoader)
- AI-powered document understanding — layout analysis, table extraction, OCR
- Uses OCR engines (RapidOCR, EasyOCR, Tesseract) to extract text from scanned/image-based pages
- **Heavyweight** — requires model downloads (modelscope.cn), high memory usage
- Memory issues when processing large documents (preprocessing renders every page to an image)
- Better structured output for RAG pipelines (chunking, metadata extraction)

## Key Issues Encountered

### 1. OCR Model Download Timeout
- RapidOCR tries to download models from `www.modelscope.cn`
- Network connectivity to modelscope may be slow or blocked
- **Fix**: Pre-download model files, use a proxy/VPN, or switch OCR engine

### 2. std::bad_alloc (Out of Memory)
- Docling's preprocessing stage renders each PDF page to an image (at `images_scale` resolution)
- With 125+ pages, memory is exhausted
- **Fix**: Process in smaller `page_range` batches, or reduce `images_scale`

### 3. OCR Engine Selection
- RapidOCR is the default (uses torch backend)
- Alternative OCR engines can be configured via `ocr_options`

## Solutions

| Problem | Solution |
|---------|----------|
| Network timeout downloading models | Pre-download once (models cache in site-packages) |
| Out of memory | Process pages in batches via `convert_kwargs={"page_range": (start, end)}` |
| Scanned pages no text | Enable OCR with `do_ocr=True` |
