# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def rle_encode(data):
    if data == "":
        return ""
    encoded = []
    length = 1
    for i in range(1, len(data)):
        if data[i] == data[i-1]:
            length+=1
        else:
            encoded.extend([str(length), str(data[i-1])])
            length = 1
    encoded.extend([str(length), str(data[-1])])
    return "".join(encoded)

def rle_decode(data):
    if data == "":
        return ""
    decoded = []
    length = 0
    for ch in data:
        if ch.isnumeric():
            length = 10*length +int(ch)
        else:
            decoded.append(length*ch)
            length = 0
    return "".join(decoded)

file = open('sem5_task4.txt', 'w')
file.write(input('введите последовательность для архивации '))
file.close

file = open('sem5_task4.txt', 'r')
f = file.read()
file.close

encoded_file = open('encoded.txt', 'w')
encoded_file.write(rle_encode(f))
encoded_file.close


encoded_file = open('encoded.txt', 'r')
en_f = encoded_file.read()
encoded_file.close

decoded_file  = open('decoded.txt', 'w')
decoded_file.write(rle_decode(en_f))
decoded_file.close