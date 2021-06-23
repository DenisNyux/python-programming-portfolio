import json


def list_to_prettystring(list_of_lists: list) -> str:
    """Возвращает список отформатированных под таблицу строк"""
    new_list = list()
    for each_list in list_of_lists:
        new_list.append(list(map(lambda x: str(x).center(30, ' '), each_list)))
    new_list = list(map(lambda x: '|'.join(x) + '\n' + '-' * len('|'.join(x)), new_list))
    new_list = '\n'.join(new_list)
    return new_list


def make_table(dcts: list) -> str:
    """Возвращает список строк из списка словарей"""
    table = list()
    # Извлекаем первую строчку в которой будут ключи
    first_line = list(dcts[0].keys())
    # Извлекаем остальные строки со значениями
    table.append(first_line)
    for i in range(0, len(dcts)):
        table.append(list(dcts[i].values()))
    return list_to_prettystring(table)


def get_from_file():
    with open('MOCK_DATA.json') as js_file:
        dicts = json.loads(''.join(js_file.readlines()))
    return dicts


def main():
    js_dicts = get_from_file()
    table = make_table(js_dicts)
    print(table)


if __name__ == '__main__':
    main()
