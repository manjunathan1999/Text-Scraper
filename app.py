from bs4 import BeautifulSoup
import docx
from PyPDF2 import PdfReader
import requests
import os

filepath = " "  ## Add the path to the file you want to scrape or https/http link

class docScraper:
    def __init__(self, file_path=filepath):
        self.file_path = file_path

    def scrape_html(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        title = soup.title.string
        paragraphs = [paragraph.get_text() for paragraph in soup.find_all('p')]
        # print(title, paragraphs)
        return title, paragraphs

    def scrape_docx(self):
        doc = docx.Document(self.file_path)
        extracted_text = []
        for paragraph in doc.paragraphs:
            extracted_text.append(paragraph.text)
            # print(extracted_text)
        return extracted_text

    def scrape_text(self):
        with open(self.file_path, 'r') as file:
            content = file.read()
        lines = content.split('\n')
        # print(lines)
        return lines

    def scrape_pdf(self):
        with open(self.file_path, 'rb') as file:
            pdf_reader = PdfReader(file)
            extracted_text = []
            for page in pdf_reader.pages:
                extracted_text.append(page.extract_text())
                # print(extracted_text)
        return extracted_text

    def scrape_file(self):
        if self.file_path.startswith(('http://', 'https://')):
            response = requests.get(self.file_path)
            if response.status_code == 200:
                content_type = response.headers.get('Content-Type', '').lower()
                if content_type.startswith('text/html'):
                    return self.scrape_html(response.text),
                else:
                    print("Unsupported content type:", content_type)
            else:
                print("Failed to retrieve the URL:", response.status_code)
        else:
            file_extension = os.path.splitext(self.file_path)[-1].replace(".","")
            
            def scrape_html():
                return self.scrape_html(open(self.file_path, 'r').read()),

            def scrape_docx():
                return self.scrape_docx(),

            def scrape_text():
                return self.scrape_text(),

            def scrape_pdf():
                return self.scrape_pdf(),
                
            switch = {
            'html': scrape_html,
            'docx': scrape_docx,
            'txt': scrape_text,
            'pdf': scrape_pdf
            }

            return switch.get(file_extension, lambda: print("Unsupported file extension:", file_extension))()


doc = docScraper()
print(doc.scrape_file())