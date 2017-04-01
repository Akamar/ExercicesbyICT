# Input matrix elements

#welcome table
print('Введите ваше имя и группу')

StudName=str(input())
StudGroup=str(input())

print('Добро пожаловать,', StudName, 'из', StudGroup, 'группы')

print('Вводите элементы построчно')
print('‖a11 a12 | b1‖')
print('‖a21 a22 | b2‖')

a11=float(input())
a12=float(input())
b1=float(input())
a21=float(input())
a22=float(input())
b2=float(input())

# criteria

if (a22==0 and a21==0) or (a12==0 and a11==0):
        print('no solutions')
elif (a11==0 and a21==0) or (a12==0 and a22==0):
        print('infinite')

# evaluations

c=a21/a11
x2=(b2-b1*c)/(a22-a12*c)
x1=(b1-a12*x2)/a11

print('x1 = ', x1)
print('x2 = ', x2)
