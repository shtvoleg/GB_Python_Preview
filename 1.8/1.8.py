# Занятие 1 (07.04.2023).
#
# Задача 8 (без циклов):
#
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите размер шоколадки по вертикали (n): "))
m = int(input("Введите размер шоколадки по горизонтали (m): "))
k = int(input("Введите число долек (k): "))
if n<=0 or m<=0 or k<=0:
    print("Все числа должны быть >0")
elif k%m==0 or k%n==0:
    print(f"{n} {m} {k} -> yes")
else:
    print(f"{n} {m} {k} -> no")