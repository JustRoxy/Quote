import requests
from bs4 import BeautifulSoup
##raw = "Наступило молчание. Графиня глядела на гостью, приятно улыбаясь, впрочем, не скрывая того,"
##raw = "Horatio says 'tis but our fantasy, And will not let belief take hold of him"
##raw = "Он стал уединяться и избегать людей. Служба и раньше была ему противна, теперь же она стала для него невыносима. Он боялся,"
##raw = "To be sure we have harvested: but why have all our fruits become rotten and brown? What was it fell last night from the evil moon?"
##raw = "Святой стал смеяться над Заратустрой и так говорил: «Тогда постарайся, чтобы они приня-ли твои сокровища! Они недоверчивы к отшельникам и не верят, что мы приходим, чтобы да-рить."

def mainFunc(raw):
	raw = raw.split(' ')
	currentstring = ''
	newraw = []
	for i in raw:
		for j in i:
			if j == ',':
				currentstring += '%2C'
			else:
				currentstring += str(j)
		newraw.append(currentstring)
		currentstring = ''
	newraw = "+".join(newraw)
	link = "http://www.google.ru/search?tbm=bks&hl=ru&q="+newraw+"&num=1"
	response = requests.get(link)
	soup = BeautifulSoup(response.text, 'html.parser')
	bookname = str(soup.find_all("h3", class_="r")).split('">')[2].split('</a>')[0].split('&amp;')[0]
	print('Скорее всего это: ', bookname)
	author = str(soup.find_all("span", class_="f")).split('a class="fl"')[1].split('>')[1].split('<')[0]
	print('Автора: ', author)
	print(" ")
	
	return([bookname, author])


if __name__ == "__main__":
	while True:
		raw = input("Ну что-с, давайте сюда вашу цитатку: ")
		raw = "Наступило молчание. Графиня глядела на гостью, приятно улыбаясь, впрочем, не скрывая того,"	
		returned = mainFunc(raw)
		author = returned[1]
		book = returned[0]
