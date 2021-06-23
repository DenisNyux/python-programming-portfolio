# Тема 7. Тестирование
## Нюхалов Денис, ИВТ2
Программа для тестирования в заданиях ИСР и ВСР
```python
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

```
### Инвариантная самостоятельная работа


Задание 1:
```python
import main


print(main.list_to_prettystring([[], []]))


try:
    assert type(main.make_table([{'a': '1'}, {'b': '2'}])) == type(str())
except:
    print('It`s not a list of dicts')
try:
    assert type(main.list_to_prettystring([[1, 2], [3, 4]])) == type(str())
except:
    print('It`s not list of lists')
try:
    assert type(main.list_to_prettystring([[1, 2], [3, '4']])) == type(str())
except:
    print('It`s not list of lists')
try:
    assert type(main.get_from_file()) == type(dict())
except:
    print('Vals from file imported not as a dict')

```
Результат: 

![Alt text](/results/i1.png)


Задание 2:
```python
import json
import doctest


def list_to_prettystring(list_of_lists: list) -> str:
    """
    >>> type(list_to_prettystring([[], []]))
    <class 'str'>
    >>> type(list_to_prettystring([[1, 2], [3, '4']]))
    <class 'str'>
    """
    new_list = list()
    for each_list in list_of_lists:
        new_list.append(list(map(lambda x: str(x).center(30, ' '), each_list)))
    new_list = list(map(lambda x: '|'.join(x) + '\n' + '-' * len('|'.join(x)), new_list))
    new_list = '\n'.join(new_list)
    return new_list


def make_table(dcts: list) -> str:
    """
    >>> type(make_table([{'a': '1'}, {'b': '2'}]))
    <class 'str'>
    """
    table = list()
    # Извлекаем первую строчку в которой будут ключи
    first_line = list(dcts[0].keys())
    # Извлекаем остальные строки со значениями
    table.append(first_line)
    for i in range(0, len(dcts)):
        table.append(list(dcts[i].values()))
    return list_to_prettystring(table)


def get_from_file():
    """
    >>> type(get_from_file()) == type(dict())
    <class 'dict'>
    """
    with open('MOCK_DATA.json') as js_file:
        dicts = json.loads(''.join(js_file.readlines()))
    return dicts


def main():
    js_dicts = get_from_file()
    table = make_table(js_dicts)
    print(table)


if __name__ == '__main__':
    main()
    doctest.testmod()
```

Результат: 

![Alt text](/results/i2.png)

Задание 3:

```python
import main
import pytest

def tests():
    assert type(main.make_table([{'a': '1'}, {'b': '2'}])) == type(str())
    assert type(main.list_to_prettystring([[1, 2], [3, 4]])) == type(str())
    assert type(main.list_to_prettystring([[1, 2], [3, '4']])) == type(str())
    assert type(main.get_from_file()) == type(dict())


tests()
```

Результат: 

![Alt text](/results/i3.png)


## Вариативная самостоятельная работа

[Задание 1](https://github.com/python-basic/sem3-t4-DenisNyux/blob/master/VSR/task1.pdf)

Задание 2:
```python
import unittest
import main


class TestTableMethods(unittest.TestCase):

    def test_maketable_is_str(self):
        self.assertEqual(type(main.make_table([{'a': '1'}, {'b': '2'}])), type(str()))

    def test_lst_to_str(self):
        self.assertEqual(type(main.list_to_prettystring([[1, 2], [3, 4]])), type(str()))
        self.assertEqual(type(main.list_to_prettystring([[1, 2], [3, '4']])), type(str()))

    def test_file_extr(self):
        self.assertEqual(type(main.get_from_file()), type(dict()))


TestTableMethods()

```

![Alt text](/results/v2.png)