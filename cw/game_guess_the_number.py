def main():
    # Чтение числа из файла
    try:
        with open("D:/TSU/numbers.txt", "r") as file:
            number = int(file.read().strip())
    except FileNotFoundError:
        print(
            "Файл numbers.txt не найден. Пожалуйста, создайте его и поместите туда число."
        )
        return
    except ValueError:
        print(
            "Ошибка в файле numbers.txt. Пожалуйста, убедитесь, что там находится корректное число."
        )
        return

    # Основная логика игры
    attempts = 0
    print("Игра началась! Угадайте число:")
    while True:
        guess = int(input("Введите ваше предположение: "))

        attempts += 1

        if guess == number:
            print(f"Правильно! Вы угадали число {number} за {attempts} попыток.")
            break
        elif guess > number:
            print("Ваше число больше загаданного. Попробуйте еще раз.")
        else:
            print("Ваше число меньше загаданного. Попробуйте еще раз.")


if __name__ == "__main__":
    main()
