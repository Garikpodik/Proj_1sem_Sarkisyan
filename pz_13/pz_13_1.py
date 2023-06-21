# В матрице найти минимальный элемент в предпоследнем столбце.

from random import randint

len_m = int(input('Введите размер матрицы: '))  # ввод размер матрицы

matrix =[]
matrix = [[randint(-100, 100) for _ in range(len_m)] for _ in range(len_m)] # создание матрицы
#for i in matrix:
 #   print(*i, sep='\t' )

b = list(matrix[:-1])

#for i in b:
 #  min=min(i)


print(f'Матрица:{matrix},\n Минимальный элемент предпсоледнего стобца:{b}')