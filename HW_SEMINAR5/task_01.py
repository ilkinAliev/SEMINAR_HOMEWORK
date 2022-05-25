#Напишите программу, удаляющую из текста все слова, содержащие "абв".

my_str = 'Напишите програбвмму, удаляющую из текста все 456 словабв, содержащие "абв"'

#ВРИАНТ №1
# my_str1 = my_str.split()
# result = ''
# for word in my_str1:
#     if word.find('абв') == -1:
#         result += word + ' '
# print(f'{my_str}\n{result}')

#ВАРИАНТ №2
# result = " ".join(map(str, [x for x in my_str.split() if x.find('абв') == -1])) # преобразование в строку, если есть итерируемые значения int
result = " ".join( [x for x in my_str.split() if x.find('абв') == -1])
print(result)