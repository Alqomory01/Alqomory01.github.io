import requests
from bs4 import BeautifulSoup

url = "https://digitalfortressltd.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

with open('file.html', 'wt', encoding='utf-8') as file:
    file.write(soup.prettify())
    file.write('\n')