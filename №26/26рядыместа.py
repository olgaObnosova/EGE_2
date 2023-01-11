f = open('26_ryd.txt') # Открыл в Excel,
# отсортировал по столбцу А (по рядам в порядке убывания)
# затем добавил в Excel второй уровень сортировки
# отсортировал вторым уровнем по местам в порядке убывания
# скопировал все в файл txt и открыл в питоне

a = [line.split() for line in f]    # считал по 2 числа - ряды и места
# Так как в файлах может содержаться любая информация,
# То питон по умолчанию считывает все как строки
# Поэтому сейчас у нас а переменной а находится список кортежей из строк

r = []    # отлельно список рядов   
m = []    # отдельно список мест

for i in a: # Проходимся по а
    sdf = [int(x) for x in i]
    #print(sdf)# Превращаем строки в числа
    #print(sdf[0],sdf[1])
    for j in range(0, len(sdf), 2):
        
        # теперь проходимся по числам
        r.append(sdf[j])    # добавляем отдельно в списки ряды
        m.append(sdf[j + 1])    # и добавляем отдельно места

'''
Условие такое: если ряды равны и одно свободное место между двумя, то есть
Если ряды равны и разность между местами равна 2:
то такие ряды и места нам подходят, среди них ищем максимум
'''

tec_r = 0    # текущее значение ряда, в него сохраняем r[i], если ряды равны, т.е. если это один и тот же ряд
tec_m = 0    # текущее значение места, в него сохраняем m[i], если места отличаются на 2

max_r = 0    # Максимальный ряд
max_m = 0    # Максимальное место

fr = False    # Флажок выполнения условия для рядов
fm = False    # Флажок выполнения условия для мест

for i in range(len(r) - 1): # Условие для рядов 
    if r[i] == r[i + 1]: # Если ряды равны (т.е. если это один и тот же ряд)
        tec_r = r[i] # То созраняем текущее значение
        fr = True # Наше условие выполнено, ставим флажок на True
print(tec_r)

for i in range(len(m) - 1): # Условие для мест
    if fr == True: # Проверяем, выполнено ли условие для рядов. 
        if abs(m[i] - m[i + 1]) == 2: # Если места находятся на одном ряду, то проверяем их разность 
            tec_m = m[i] # Если это условие выполнено, то сохраняем текущее
            fm = True # И ставим флажок на True


if (fr == True and fm == True): # Если оба условия выполнены
    max_r = max(tec_r, max_r) # То пусть наш максимум - это то самое текущее
    max_m = max(tec_m, max_m) # Аналогично для мест

    # Ну и так каждый раз текущее будет перезапиываться в циклах
    # И считать максимум

print(max_r, max_m) # Выводим максимальный ряд и максимальное место










        
        
