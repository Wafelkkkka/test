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

delenie = len(viborka) // 2
first_vib = viborka[:delenie]
second_vib = viborka[delenie:]

first_result = number_search(first_vib, number)
second_result = number_search(second_vib, number)

if first_result:
    print("Тут есть :)")
elif second_result:
    print("Тут тоже есть ;)")
else:
    print(":(")
