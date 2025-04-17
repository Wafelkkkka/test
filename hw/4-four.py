import math

units = {
    0: "ноль",
    1: "один",
    2: "два",
    3: "три",
    4: "четыре",
    5: "пять",
    6: "шесть",
    7: "семь",
    8: "восемь",
    9: "девять",
    10: "десять",
    11: "одиннадцать",
    12: "двенадцать",
    13: "тринадцать",
    14: "четырнадцать",
    15: "пятнадцать",
    16: "шестнадцать",
    17: "семнадцать",
    18: "восемнадцать",
    19: "девятнадцать",
}
tens = {
    2: "двадцать",
    3: "тридцать",
    4: "сорок",
    5: "пятьдесят",
    6: "шестьдесят",
    7: "семьдесят",
    8: "восемьдесят",
    9: "девяносто",
}


def slova(num):
    if num < 20:
        return units[num]
    elif num < 100:
        tens_digit = num // 10
        ones_digit = num % 10
        return (
            f"{tens[tens_digit]} {units[ones_digit]}"
            if ones_digit
            else tens[tens_digit]
        )


while True:
    user_input = input("Введите число от 0 до 99:")

    try:
        num = int(user_input)
        if 0 <= num <= 99:
            print(slova(num))
        else:
            print("Введенное число должно быть от 0 до 99.")
    except ValueError:
        print("Вы должны ввести число.")
