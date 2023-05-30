# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
#
# *Пример:*
#
# **Ввод:** `print_operation_table(lambda x, y: x * y) `
# **Вывод:**
#  1  2  3  4  5  6
#  2  4  6  8 10 12
#  3  6  9 12 15 18
#  4  8 12 16 20 24
#  5 10 15 20 25 30
#  6 12 18 24 30 36

from functools import reduce

"""
    Чудо-функция выводит таблицу по заданным параметрам: бинарная операция и размерность
"""
def print_operation_table(operation, num_rows=6, num_columns=6):

    rows = list(range(1, num_rows + 1))                     # диапазон строк
    cols = list(range(1, num_columns + 1))                  # диапазон столбцов

    # матрица, каждый элемент равен бинарной операции между номером строки и номером столбца
    matrix = list(map(lambda row: list(map(lambda col: operation(row, col), cols)), rows))

    # вывод матрицы с виде таблицы (нумерация строк и столбцов - с 1; без обозначения по условиям задачи)
    matrix_str = reduce(lambda x, y: x + '\n' + y, map(lambda row: '\t'.join(map(str, row)), matrix))
    print(matrix_str)


# (copy+paste):   print_operation_table(lambda x, y: x * y)  или:     print_operation_table(lambda x, y: x + y, 7, 10)
my_input = input('Введите выражение типа "print_operation_table(lambda x, y: x + y, 7, 10)", вычисляющее элемент по номеру строки и столбца: ').strip()

# проверка делителя на 0
counter = my_input.count(',')
if counter == 3:
    my_split = my_input.split(",")[3].strip()
    my_divider = int(my_split.split(")")[0].strip())
    if my_divider == 0:
        print("Последнее число не должно быть 0!")

# Вызов чудо-функции
my_function = eval(my_input)                                  # чтобы отрезать кавычки

# 1-й пример использования:
# Введите функцию, вычисляющую элемент по номеру строки и столбца: print_operation_table(lambda x, y: x * y)
# 1	 2	3	4	5	6
# 2	 4	6	8	10	12
# 3	 6	9	12	15	18
# 4	 8	12	16	20	24
# 5	 10	15	20	25	30
# 6	 12	18	24	30	36

# 2-й пример использования:
# Введите функцию, вычисляющую элемент по номеру строки и столбца: print_operation_table(lambda x, y: x + y, 7, 10)
# 2	 3	4	5	6	7	8	9	10	11
# 3	 4	5	6	7	8	9	10	11	12
# 4	 5	6	7	8	9	10	11	12	13
# 5	 6	7	8	9	10	11	12	13	14
# 6	 7	8	9	10	11	12	13	14	15
# 7	 8	9	10	11	12	13	14	15	16
# 8	 9	10	11	12	13	14	15	16	17