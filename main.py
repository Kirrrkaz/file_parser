#pip install beautifulsoup4
#pip install lxml

from bs4 import BeautifulSoup
with open("index.html", encoding='utf-8') as file:
    src = file.read()
#print(src)

soup = BeautifulSoup(src, 'html.parser')

user_name = soup.find("div", class_="user__name")
print('User name: ', user_name.text)



title = soup.title
print(title.text)

links = soup.find_all("a")
print(links)
print('List of the users social networks:')
for item in links:
    print(item.text)

k = input("press to exit")



