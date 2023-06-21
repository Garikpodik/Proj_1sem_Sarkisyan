#.Даны текущие оценки студента по дисциплине «Основы программирования» за месяц.
# Необходимо найти количество «2», «3», «4» и «5»,
# полученных студентом, и определить итоговую оценку за месяц.

from random import randint
from statistics import mean

n = int(input(''))
num = [randint(2, 5) for i in range(n)]


len_2 = len([int(i) for i in num if int(i) == 2])
len_3 = len([int(i) for i in num if int(i) == 3])
len_4 = len([int(i) for i in num if int(i) == 4])
len_5 = len([int(i) for i in num if int(i) == 5])

print(f'Все оценки студента: {num} \nКол-во 2:{len_2} \nКол-во 3:{len_3} \nКол-во 4:{len_4} \nКол-во 5:{len_5}\nСреднее арифметическое:{round(mean(num))}')




