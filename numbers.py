import math


def number_search(viborka, number):
    if number in viborka:
        return True
    else:
        return False


viborka = [
    23,
    57,
    1,
    10,
    115,
    34,
    466,
    7,
    2,
    5,
    0,
    46,
    77,
    55,
    31,
    32,
    64,
    11,
    33,
    3,
    4,
    7,
    9,
    83,
    100,
    101,
    99,
    12,
    13,
]
number = float(input("Введите число:"))

result = number_search(viborka, number)

if result:
    print("Число есть!")
else:
    print("Числа нет.")
