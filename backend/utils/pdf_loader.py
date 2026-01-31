from PyPDF2 import PdfReader

def load_pdf_and_chunk(file_path: str, chunk_size=500, overlap=100):
    reader = PdfReader(file_path)

    full_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"

    full_text = full_text.strip()
    if not full_text:
        return []

    chunks = []
    start = 0

    while start < len(full_text):
        end = start + chunk_size
        chunks.append(full_text[start:end])
        start += chunk_size - overlap

    return chunks
