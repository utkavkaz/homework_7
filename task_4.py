"""
Задание 4.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""
from random import randint

try:
    class Matrix:

        def __init__(self):
            self.matrix = []
            x = int(input("Введите количество столбцов матрицы: "))
            for i in range(x):
                a = []
                for j in range(x):
                    a.append(randint(-5, 5))
                self.matrix.append(a)

        def __str__(self):
            matrix_str = []
            for i in self.matrix:
                matrix_str.append('  '.join([str(j) for j in i]))
            return '\n'.join(matrix_str)

        def __add__(self, other):
            sum_matrix = []
            for item in zip(self.matrix, other.matrix):
                sum_matrix.append([sum([i, j]) for i, j in zip(*item)])
            return '\n'.join('  '.join(str(i) for i in j) for j in sum_matrix)


    matrix_1 = Matrix()
    matrix_2 = Matrix()

    print(matrix_1)
    print()
    print(matrix_2)
    print()
    print(matrix_1 + matrix_2)
except ValueError:
    print("Вводите число!")
