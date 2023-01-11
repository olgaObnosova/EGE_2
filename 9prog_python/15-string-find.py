# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 15. Поиск и замена
#

s = "Здесь был Вася."
n = s.find( "с" )		# n = 3
if n >= 0:
  print( "Номер символа", n )
else:
  print( "Символ не найден." )

s = "Здесь был Вася."
n = s.rfind( "с" )	   # n = 12
if n >= 0:
  print( "Номер символа", n )
else:
  print( "Символ не найден." )

date = "12/02/2018"
dateRus = date.replace("/", ".") # "12.02.2018"
print( dateRus )

dateRus = date.replace("/",".",1) # "12.02/2018"
print( dateRus )



