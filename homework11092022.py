# 1. Вычислить число c заданной точностью d Пример:
#- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
# num = float(input('введите число '))
# d = float(input('введите точность ')) #точность
# s = str(d)
# dd = (abs(s.find('.') - len(s)) - 1)
# print(round(num,dd))

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# num = int(input('Введите число '))
# print("делители: ", end=" ")
# for i in range(num-1,1,-1):
#     simple_num = 0
#     if (num%i == 0):
#         for j in range(i-1,1,-1):
#             if (i % j == 0):
#                 simple_num = simple_num + 1
#         if (simple_num == 0):
#             print(i, end = " ")

# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# list = [1,1,'abcd',2,3,3,4,4,5,5,'abcd',6,7,7,8,8,999]
# unic_list = set()
# for elem in list:
#     unic_list.add(elem)
# print(unic_list)

# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k. Пример:- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint
k = int(input('Введите натуральную степень k = '))
koeff = []
f = open('urav.txt','w')  # открытие в режиме записи
for i in range(k):
    koeff.append(randint(0,100))
    f.write(str(koeff[i]))  # запись  файл
    f.write(str('x^'))
    f.write(str(k-i))
    f.write(str('+'))
last_index = randint(0,100)
f.write(str(last_index))
f.write(str('=0'))
f.close()
print(koeff)




