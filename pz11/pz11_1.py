# Средствами языка Python сформировать два текстовых файла (.txt),
# содержащих по одной последовательности из целых положительных и отрицательных чисел.
# Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Содержимое первого файла:
# Четные элементы:
# Количество четных элементов:
# Среднее арифметическое:
# Содержимое второго файла:
# Нечетные элементы:
# Количество нечетных элементов:
# Сумма положительных элементов:



from random import randint
from statistics import mean

f1 = open('num_1.txt', 'w')  # создание первого файла
f1.write(' '.join([str(randint(-100, 100)) for i in range(10)]))  # добавление данных в файл
f1.close()

f2 = open('num_2.txt', 'w')  # создание второго файла
f2.write(' '.join([str(randint(-100, 100)) for i in range(10)]))  # добавление данных в файл
f2.close()


f3 = open('num_3.txt', 'w', encoding='UTF-8')  # создание заполняемого файла
f4 = open('num_1.txt', 'r', encoding='UTF-8').read()  # чтение первого файла


sr_arifm = mean(int(i) for i in f4.split(' ') )
chet = list(filter(lambda x: x%2==0, [int(i) for i in f4.split(' ')]))
len_chet = len(chet)

f5 = open('num_2.txt', 'r', encoding='UTF-8').read()

nechet = list(filter(lambda x: x%2==1, [int(i) for i in f5.split(' ')]))
len_nechet = len(nechet)
#sum_num = sum([int(i) for i in f5.split(' ')])
#for i in f5.split(' '):

#sum_num = sum(i for i in f5.split(' ') if i > 0, [int(i) for i in f5.split(' ')])
#sum_num = sum(list(filter([i for i in f5.split('') >0],[int(i) for i in f5.split(' ')])))
#sum_num = sum([int(i) for i in f5.split(' ')[i in f5.split(' ')>0]])
sum_num = sum([int(i) for i in f5.split(' ') if int(i) > 0])
f3.write(f'Содержимое первого файла: {f4}\n')  # получаем исходные данные
f3.write(f'Четные элементы: {chet}\n')
f3.write(f'Количество четных элементы: {len_chet}\n')
f3.write(f'Среднее арифметическое: {sr_arifm}\n\n')
f3.write(f'Содержимое второго файла: {f5}\n')
f3.write(f'Четные элементы: {nechet}\n')
f3.write(f'Количество четных элементы: {len_nechet}\n')
f3.write(f'Количество четных элементы: {sum_num}\n')

f3.close()  # закрываем файл