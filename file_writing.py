from user_interface import get_info as gi

info = gi()
def writing_csv ():
    file = 'phonebook.csv'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')

def writing_txt ():
    file = 'phonebook.txt'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'Фамилия: {info[0]}\n\nИмя: {info[1]}\n\nНомер телефона: {info[2]}\n\nОписание: {info[3]}\n\n\n')
