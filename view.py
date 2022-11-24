def view_data(data, title):
    print(f'{title}{data}')
    
def get_value():
    while True:
        try:
            return int(input('Введите число: '))
        except ValueError:
            print('Вы ввели не число! Введите число!')

def operacia():
    while True:
        i = str(input('Введите операцию: '))
        if i in ['*', '/', '+', '-']:
            return i
        else:
            pass
