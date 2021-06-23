import math


test_values = ((2, 1, 2, 0.96824), (3, 4, 5, 6.0))
"""
print('Сколько тестов вы хотите сделать? ', end = '')
amount = int(input())
while amount != 0:
    print('Введите значения:')
    first_val = float(input())
    second_val = float(input())
    third_val = float(input())
    fourth_val = float(input())
    temp_list = [first_val, second_val, third_val, fourth_val]
    test_values.append(temp_list)
    amount -= 1
"""


def tests(func):
    try:
        for val in test_values:
            assert round(func(val[0], val[1], val[2]), 5) == val[3], "Wrong counting"
    except:
        print(round(func(val[0], val[1], val[2]), 5), val[3])
        for val in test_values:
            assert type(func(val[0], val[1], val[2])) == float, "Wrong type"


def g_square(a: float, b: float, c: float) -> float:
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


def main():
    a = float(input('a: '))
    b = float(input('b: '))
    c = float(input('c: '))

    assert b + c >= a, "it`s not a triangle"
    assert a + c >= b, "it`s not a triangle"
    assert a + b >= c, "it`s not a triangle"

    print('Результат: ', round(g_square(a, b, c), 5))


main()


if __name__ == "__main__":
    tests(g_square)

