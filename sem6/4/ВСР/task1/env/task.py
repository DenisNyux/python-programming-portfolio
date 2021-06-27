num_names = [
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'    
]


def starry_sky(number, type='dec', names_arr = num_names):
    
    if number<0 and number>9:
        print('Wrong number!!!')
        return None
    
    if type == 'dec':
        print(names_arr[number])
    elif type == 'bin':
        print(bin(number))
    elif type == 'oct':
        print(oct(number))
    elif type == 'hex':
        print(hex(number))
    else:
        print('Wrong type!!!')
    

def main():
    num = int(input('Введите число: '))
    type = input('Введите тип числа (если десятеричное - не вводите ничего или введите dec): ')
    if num not in range(0, len(num_names)):
        print('Wrong number!!!')
    else:
        if type == None:
            starry_sky(num)
        else:
            starry_sky(num, type)


main()