import sys
import requests
from bs4 import BeautifulSoup

def strip_html_tags(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text()
    return text

def download_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4XX or 5XX status codes
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python anti_html.py <url>")
        sys.exit(1)

    url = sys.argv[1]

    html_content = download_html(url)
    text_without_html = strip_html_tags(html_content)
    print(text_without_html)
