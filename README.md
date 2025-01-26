## Description

The python script is designed to extract and process text content from various file types, including HTML, DOCX, TXT, and PDF files. It provides a simple interface for scraping text data from either local files or URLs. This can be particularly useful for applications like text analysis, document processing, or data extraction.

## Features
- HTML Scraping:

    Extracts the title and all paragraph content (<p> tags) from an HTML document.
    Accepts either raw HTML content or a URL pointing to an HTML file.

- DOCX Scraping:

    Reads .docx files (Microsoft Word format) and extracts the text from all paragraphs.

- Text File Scraping:

    Reads .txt files and returns their content, line by line.

- PDF Scraping:

    Extracts text from all pages of a PDF file using PyPDF2.

- Automatic File Type Detection:

    Automatically determines the file type based on the file extension or the content type of a URL.

- Modular Design:

    The class-based design allows easy integration and extensibility for additional file formats or scraping methods.

## Requirements

    pip install beautifulsoup4 python-docx PyPDF2 requests


## Clone the Repository

    git clone https://github.com/manjunathan1999/Text-Scraper.git
    cd Text-Scraper

## Error Handling

The script handles common errors including:
- Invalid URLs
- Connection timeouts
- Missing permissions
- Server errors

## License

MIT License

## Contributions

Contributions are welcome! Feel free to submit a pull request or open an issue for discussion.