# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('задайте число '))
n1 =n
res = []
def func(i):
    global n1
    global res
    while (n1 % i == 0):
        n1 //= i
        res.append(i)

list(map(func, [i for i in range(2, int(n**0.5)+1)]))
if (n1 != 1):
    res.append(n1)

print(res)
