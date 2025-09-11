from langchain_core.tools import tool
import requests
from bs4 import BeautifulSoup

@tool
def scrape_and_clean_url(url: str) -> str:
    """
    Scrapes a URL and returns clean, readable text from the page.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        return f"Error fetching URL: {e}"
    soup = BeautifulSoup(response.text, 'html.parser')
    for tag in soup(['script', 'style', 'noscript']):
        tag.decompose()
    text = soup.get_text(separator='\n')
    clean_text = '\n'.join(line.strip() for line in text.splitlines() if line.strip())
    max_chars = 5000
    return clean_text[:max_chars] + ("\n...[truncated]" if len(clean_text) > max_chars else "")