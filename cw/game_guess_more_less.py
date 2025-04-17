
def read_number_from_file(file_path):
    with open(file_path, "r") as file:
        return int(file.read().strip())


def play_game(number):
    attempts = 0
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
    # Загружаем число из файла numbers.txt
    try:
        number = read_number_from_file("D:/TSU/numbers.txt")
        print("Игра началась! Угадайте число:")
        play_game(number)
    except FileNotFoundError:
        print(
            "Файл numbers.txt не найден. Пожалуйста, создайте его и поместите туда число."
        )
    except ValueError:
        print(
            "Ошибка в файле numbers.txt. Пожалуйста, убедитесь, что там находится корректное число."
        )
