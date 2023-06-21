#Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее элементов.

from random import randint

len_m = int(input('Введите размер матрицы: '))  # ввод размер матрицы

matrix = [[randint(-100, 100) for _ in range(len_m)] for _ in range(len_m)] # создание матрицы

