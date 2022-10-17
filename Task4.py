# Напишите программу, которая будет преобразовывать десятичное число
# в двоичное.
array=[]
a=int(input('Введите целое число: '))
b = a
for i in range(a):
    if a==1:
        array.append(1)
        break
    elif a%2==1:
        array.append(1)
        a=(a-1)/2
    elif a%2==0:
        array.append(0)
        a=a/2
print(b, ' = ',*array[::-1], sep='')
