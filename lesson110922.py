# 1. задайте строку из набора чисел. напишите программу, которая покажет большее и меньшее число. в качестве символа разделителя использовать пробел
# some_str = input()
# some_list = some_str.split()
# some_int_list = list(map(int, some_list)) # map всегда надо распаковывать
# print(max(some_int_list), min(some_int_list))

# 2. Найти корни квадратного уравнения
# a = int(input())
# b = int(input())
# c = int(input())
# d = b**2 - 4*a*c
# if d<0:
#     print('корней нет')
# elif d == 0:
#     print(-b/2*a)
# else:
#     print((-b+d**(1/2))/2*a)
#     print((-b-d**(1/2))/2*a)
# import sympy as sm

# x = sm.Symbol('x')
# a = int(input())
# b = int(input())
# c = int(input())
# print(sm.solveset(a*x**2+b*x+c,x))

# 3. задайте 2 числа. найдите НОК
import sympy as sm
a = int(input())
b = int(input())
print(sm.lcm(a,b))