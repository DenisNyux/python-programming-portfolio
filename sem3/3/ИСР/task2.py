def main():
    input_str = input("Введите строку для поиска: ")

    searchable_str = input("Введите строку, по которой мы ищем: ")

    choice = None
    while choice != '4':
        print('1 - поиск первого вхождения подстроки')
        print('2 - замена первой подстроки')
        print('3 - найти все вхождения подстроки' )
        print('4 - для выхода')
        choice = input("Сделайте  выбор (1..4) ")
        if choice == '1':
            print('\n', search_str_first(input_str, searchable_str), '\n', sep='')
        if choice == '2':
            replacer = input('Введите то, на что стоит заменить: ')
            print('\n', search_n_replace_str(input_str, replacer, searchable_str), '\n', sep='')
        if choice == '3':
            print('\n', search_str_all(input_str, searchable_str), '\n', sep='')


def search_str_first(what, where):
    i = 0
    k = len(where)
    res = list()
    while k != 0:
        j = i + len(what)
        if what in where[i:j]:
            res.append(i)
        i += 1
        k -= 1
    if len(res) == 0:
        return 'Ничего не найдено'
    else:
        return res[0]


def search_n_replace_str(what, to_what, where):
    index = search_str_first(what, where)
    changed = where[0:index] + to_what + where[index + len(what):len(where)]
    return changed


def search_str_all(what, where):
    i = 0
    k = len(where)
    res = list()
    while k != 0:
        j = i + len(what)
        if what in where[i:j]:
            res.append(i)
        i += 1
        k -= 1
    if len(res) == 0:
        return 'Ничего не найдено'
    else:
        return res


main()
