from Prog.save import log_phonebook
from intro.initial import init_contact
from Prog.save import get_id
from OUT.out import out_dict



program = True
id = 0
phone_book = {
    id: {
        'surname': 'surname',
        'name': 'name',
        'phone_number': 'phone_number'
    }
}
operator = {1: 'посмотреть список контактов',
            2: 'добавить контакт',
            3: 'удалить контакт',
            4: 'найти номер по имени',
            5: 'выйти из программы'}
while program == True:
    for key, value in operator.items():
        print(f'{key} - {value}')
    userOperationText = int(input('введите № операции '))
        
    if userOperationText == 5:
        print('до свидания!')
        program = False
        continue

    if userOperationText == 2:
        li = init_contact()
        phone_book[get_id(phone_book)] = {'surname': li[0], "name": li[1], "phone_number": li[2]}
        out_dict(phone_book)
        log_phonebook(phone_book)
        

