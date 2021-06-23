def changer(letter):
    if ord('a') + 13 > ord(letter) >= ord('a'):
        return chr(ord(letter) + 13)
    elif ord('z') >= ord(letter) >= ord('a') + 13:
        return chr(ord(letter) - 13)
    else:
        return letter


def main():
    string_to_encrypt = input('Введите строчку которую нужно зашифровать: ')
    encrypted_res = ''.join(list((map(changer, string_to_encrypt))))
    print('Результат шифрования:', encrypted_res)


main()
