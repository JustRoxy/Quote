import requests
from bs4 import BeautifulSoup   
from urllib.parse import quote

def mainFunc(raw):
    url = "http://www.google.ru/search?tbm=bks&hl=ru&q={raw}&num=1".format(raw=quote(raw, safe=''))
    print(url)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    bookname = soup.select(".r > a")[0].get_text()
    author = soup.select(".f > a")[0].get_text()
    return bookname, author


if __name__ == "__main__":
    while True:
        raw = input("Ну что-с, давайте сюда вашу цитатку: ")
        book, author = mainFunc(raw)
        print('Скорее всего это: ', book)
        print('Автора: ', author)
        print(" ")
