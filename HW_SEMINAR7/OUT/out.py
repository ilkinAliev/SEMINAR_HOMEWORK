
def out_dict(dict):
    for key, value in dict.items():
        print(key, end =' ') 
        for i in value.values():
            print(i, end = ' ')
        print()



