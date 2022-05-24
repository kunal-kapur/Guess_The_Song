from bs4 import BeautifulSoup
import requests

page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())