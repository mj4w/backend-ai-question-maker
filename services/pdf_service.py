import fitz  # PyMuPDF

class PDFService:
    @staticmethod
    def extract_text(file_path):
        text = ""
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()
        return text.strip()
