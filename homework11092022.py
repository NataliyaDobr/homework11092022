# 1. Вычислить число c заданной точностью d Пример:
#- при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
# num = float(input('введите число '))
# d = float(input('введите точность ')) #точность
# s = str(d)
# dd = (abs(s.find('.') - len(s)) - 1)
# print(round(num,dd))