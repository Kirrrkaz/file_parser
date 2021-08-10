#pip install beautifulsoup4
#pip install lxml

from bs4 import BeautifulSoup
with open("index.html", encoding='utf-8') as file:
    src = file.read()
#print(src)

soup = BeautifulSoup(src, 'html.parser')

#title = soup.title
#print(title.text)

links = soup.find_all("li")
print(links)


