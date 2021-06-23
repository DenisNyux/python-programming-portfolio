"""
Nyukhalov Denis
IVT 2 kurs, group 3
"""
lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]

"""Задание 8"""
lst8 = lst[len(lst)//2-1::-2]
sumof8 = sum(lst8)
print(lst8, sumof8)

"""Задание 12"""
lst12 = lst[1:len(lst)//2+1:2]
sumof12 = sum(lst12)
print(lst12, sumof12)
