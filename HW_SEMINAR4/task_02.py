# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


N = int(input('Введите натуральное число для выведения списка простых множителей - '))

simples = []  # создаем пустой список для простых чисел
# для каждого возможного простого числа в диапазоне от 2 до заданного числа
for possibleSimple in range(2, N+1):
    isSimple = True  # проверяем делимость возможного простого числа без остатка на числа от двух до "возможного простого числа"
    for num in range(2, possibleSimple):
        if possibleSimple % num == 0:  # если делится без остатка на числа до "возможного простого числа", значит это число не простое
            isSimple = False
            break

    if isSimple:
        simples.append(possibleSimple)
print(simples)

smpl_multip = []
i = 0
while N > 1:
    if N % simples[i] == 0:
        smpl_multip.append(simples[i])
        N = N / simples[i]
    else:
        i += 1
print(smpl_multip)
