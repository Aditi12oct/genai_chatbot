from bs4 import BeautifulSoup
import requests

def scrape_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text(separator="\n")
    return text
if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/Generative_AI"
    content = scrape_page(url)
    print(content[:500])  # Print first 500 characters

