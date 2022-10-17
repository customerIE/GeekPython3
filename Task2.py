# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
a = [1, 2, 5, 4, 8, 10, 16]
length = int((len(a)/2))
b = []
elements = 9
for i in range(length):
    elements = a[i]*a[-i - 1]
    b.append(elements)
if len(a)%2 != 0 :
    b.append(a[length]*a[length])
print('Произведение пар чисел = ', b)
