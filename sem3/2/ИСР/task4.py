from math import *


def square(d1, d2, h):
    a = sqrt((d1/2)**2 + (d2/2)**2)
    return a*a*2 + 4*a*h


def main():
    d1 = int(input('Введите первую диагональ: '))
    d2 = int(input('Введите вторую диагональ: '))
    h = int(input('Введите высоту призмы: '))
    print('Площадь поверхности призмы:', square(d1, d2, h))


main()
