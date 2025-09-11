from langchain.document_loaders import PyPDFLoader

def load_pdf(file_path: str) -> str:
    """Load and return text content from a PDF file."""
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    return "\n".join([doc.page_content for doc in documents])

def load_text_file(file_path: str, encoding: str = 'utf-8') -> str:
    """Load and return content from a text file."""
    with open(file_path, 'r', encoding=encoding) as file:
        return file.read()