import requests
from bs4 import BeautifulSoup

goods = []
for i in range(1,28):
    url = "http://allcitations.ru/tema/citaty-iz-knig/page/"+str(i)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    raw = soup.find_all("div", {'class':'cittext'})
    for ok in raw:
        goods.append(ok.find_all('p'))
    goods = [x for x in goods if x != []]
    print(goods)