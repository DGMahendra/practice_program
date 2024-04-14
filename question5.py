import sys
import requests
from bs4 import BeautifulSoup

def remove_html_tags(text):
    # Create BeautifulSoup object to parse HTML
    soup = BeautifulSoup(text, 'html.parser')
    # Extract text from the parsed HTML
    return soup.get_text()

def main():
    if len(sys.argv) != 2:
        print("Usage: python anti_html.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        # Send GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Remove HTML tags from the response text
        clean_text = remove_html_tags(response.text)

        # Print the cleaned text
        print(clean_text)

    except requests.RequestException as e:
        print("Error fetching URL:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
