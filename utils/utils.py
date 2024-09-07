import requests
from bs4 import BeautifulSoup
import PyPDF2
import io
from fastapi import UploadFile

def scrape_url(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.get_text()

async def extract_pdf_text(file: UploadFile) -> str:
    content = ""
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(await file.read()))
    for page in pdf_reader.pages:
        content += page.extract_text()
    return content

def simple_search(query: str, content: str) -> str:
    # Simple search function that returns a part of the content containing the query
    words = content.split()
    query_words = query.lower().split()
    
    for i in range(len(words) - len(query_words) + 1):
        if all(query_word in words[i+j].lower() for j, query_word in enumerate(query_words)):
            start = max(0, i - 10)
            end = min(len(words), i + len(query_words) + 10)
            return " ".join(words[start:end])
    
    return "No relevant information found."