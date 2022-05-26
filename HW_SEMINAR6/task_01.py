# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.





from math import sqrt
n = int(input('Введите натуральное число для выведения списка простых множителей - '))
simples=[2]
for i in range(3, n+1, 2): #не проверяем числа делящиеся на 2
    if (i > 10) and (i%10==5):
        continue
    for j in simples:
        if j > int((sqrt(i)) + 1): #переберать надо только числа, не превосходящие корня из искомого
            simples.append(i)
            break
        if (i % j == 0):
            break
    else:
        simples.append(i)


smpl_multip = []
i = 0
while n > 1:
    if n % simples[i] == 0:
        smpl_multip.append(simples[i])
        n = n / simples[i]
    else:
        i += 1
print(smpl_multip)
