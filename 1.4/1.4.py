# Занятие 1 (07.04.2023).
#
# Задача 4 (без циклов):

# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?  (без циклов)
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

number = int(input("Введите общее число журавликов, кратное 6: "))
if number < 0 or number%6 != 0:
    print("Число должно быть > 0 и кратно 6!")
else:
    Peter = Serge = int(number/6)
    Kate = int(number*2/3)
    print(f"{number} -> {Peter} {Kate} {Serge}")