# input values

print('Введите число элементов будущего массива')

NumOfElem = int(input())

print('Введите массив')

List=input().split()

for i in range(len(List)):
    List[i] = int(List[i])

# eval

A = sum(list(filter((lambda x: x % 2 == 0), List)))
B = max(List)
C = min(List)
D = sum(List)/len(List)
E = sum(list(x ** 2 for x in List))

# print

print('Сумма чётных чисел --', A)
print('Максимальное число --', B)
print('Минимальное число --', C)
print('Среднее арифметическое --', D)
print('Сумма квадратов --', E)
