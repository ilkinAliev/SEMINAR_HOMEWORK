

def get_id(phone_book):
    for x in range(1, len(phone_book)+1):
        if x in phone_book:
            x+=1
        else:
            return int(x)

def log_phonebook(dict):
        with open('HW_SEMINAR7\phonebook.txt', 'w') as f:
            for key, value in dict.items():
                f.writelines(f'{key}    ') 
                for value in value.values():
                    f.writelines(f'{value}   ')
                f.write('\n')






         



    





