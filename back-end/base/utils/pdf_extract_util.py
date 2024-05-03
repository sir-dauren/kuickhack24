from PyPDF2 import PdfReader


def extract_text_from_pdf_util(file):
    """
        Вытаскивание текста из pdf
    """
    reader = PdfReader(file)
    num_pages = len(reader.pages)

    content = ''

    for page_number in range(num_pages):
        page = reader.pages[page_number]
        content += page.extract_text()

    return content