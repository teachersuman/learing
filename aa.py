import requests
from bs4 import BeautifulSoup

res = requests.get('http://www.xiachufang.com/explore/')
html = res.text
soup = BeautifulSoup(html, 'html.parser')
item = soup.find_all('p', class_='name')
list_all = []
for items in item:
    name = items.find('a')
    names = name.text.strip()
    URL = 'http://www.xiachufang.com' + name['href']
    make = items.find('p', class_="ing ellipsis")
    makes = make.text.strip()
    list_all.append([names, URL, makes])
    # print(names,'\n', URL ,'\n',makes)

print(list_all)
