# Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.
number = int(input('Введите количество последовательностей n = '))
a=[]
def fibonacci(n):
    if n in (1, 2):
        return 1
    elif n==0:
        return 0
    return fibonacci(n - 1) + fibonacci(n - 2)
for i in range(number, -1, -1):
    b = -1 * fibonacci(i)
    a.append(b)
for i in range(1,number+1):
    a.append(fibonacci(i))
print('Список чисел Фибоначчи:')
print(a)