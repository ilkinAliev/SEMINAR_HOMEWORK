# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 1 до 100,
#  можно создать свой генератор случайных чисел или использовать готовый)
#  многочлена и записать в файл многочлен степени k.
# Пример:
#     k=2 => 2*x² + 4*x + 5 = 0


from fileinput import close
import random
file = open('file.txt', 'w')
file = close
Programm = True
while Programm == True:
    k = int(input('введите натуральную степень '))
    file = open('file.txt', 'a')
    for n in reversed(range(1, k+1)):
        if n > 1:
            file.writelines(f'{random.randint(1, 101)}x^{n} + ')
            
        else:
            file.write(f'{random.randint(1, 101)}x + {random.randint(1, 101)} = 0\n')
            
    file = close