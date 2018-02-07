import requests
from bs4 import BeautifulSoup   
from urllib.parse import quote

def mainFunc(raw):
    url = "http://www.google.ru/search?tbm=bks&hl=ru&q={raw}&num=1".format(raw=quote(raw, safe=''))
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    bookname = str(soup.find_all("h3", class_="r")).split('">')[2].split('</a>')[0].split('&amp;')[0]
    author = str(soup.find_all("span", class_="f")).split('a class="fl"')[1].split('>')[1].split('<')[0]
    return bookname, author


if __name__ == "__main__":
    while True:
        raw = input("Ну что-с, давайте сюда вашу цитатку: ")
        book, author = mainFunc(raw)
        print('Скорее всего это: ', book)
        print('Автора: ', author)
        print(" ")
