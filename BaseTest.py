def testing(returned):
	bookname_test = 'Война'
	author_test = 'Толстой'
	if bookname_test in returned[0]:
		print('bookname is OK')
	else:
		print('bookname is NOTOK')
		print(bookname)
	print('    ')
	if author_test in returned[1]:
		print('author is OK')
	else:
		print('author is NOTOK')
		print(author)