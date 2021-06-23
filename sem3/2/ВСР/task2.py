def two_line_function(vals):
    res = set(vals)
    return list(sorted(res))


def main():
    print('Введите количество значений: ', end='')
    i = int(input())
    values = list()
    while i != 0:
        values.append(input())
        i -= 1
    print('Введенные значения: ', values)
    print('Уникальные значения: ', two_line_function(values))
    

main()
