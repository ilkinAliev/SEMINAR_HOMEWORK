

def init_contact():
    surname = input('Введите фамилию ')
    name = input('Введите имя ')
    phone_number = int(input('Введите номер телефона '))
    return [surname, name, phone_number]


# def read_phonebook():
#     with open ('HW_SEMINAR7\phonebook.txt', 'r') as f:
#         phone_book ={}
#         for x in f.readlines():
#             print(x.split())
#             phone_book['id'] = x[0]
#             phone_book['surname'] = x[1]
#             phone_book['name'] = x[2]
#             phone_book['phone_number'] = x[3]
#     return phone_book

