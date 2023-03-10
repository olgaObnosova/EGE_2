# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 17a. Структуры (Python 3.7+)
#

from dataclasses import dataclass

@dataclass
class TBook:
  author: str = "?"
  title: str = ""
  count: int = 0

b = TBook( "Пушкин А.С.", "Полтава", 1 )

fam = b.author.split()[0]	# только фамилия
print( fam )
b.count -= 1        		# одну книгу взяли
if b.count == 0:
  print("Этих книг больше нет!")
print( b.author, b.title + ".", b.count, "шт." )

# books = [TBook()]*100  # это ошибка!
books = []
for i in range(100):
  books.append( TBook() )

N = 100
books = [ TBook() for i in range(N) ]
