# Получение ввода от пользователя
while True:
    try:
        n = int(input("Введите число N: "))
        if n <= 1:
            print("Число должно быть больше 1. Попробуйте снова.")
            continue
        break
    except ValueError:
        print("Ошибка ввода. Введите положительное целое число.")

# Создание списка для хранения булевых значений
is_prime = [True] * (n + 1)
is_prime[0], is_prime[1] = False, False  # 0 и 1 не являются простыми числами

# Применение решета Эратосфена
for i in range(2, int(n**0.5) + 1):
    if is_prime[i]:  # Если число простое
        # Отмечаем все кратные данного числа как составные
        for j in range(i * i, n + 1, i):
            is_prime[j] = False

# Вывод всех простых чисел
for i in range(2, n + 1):
    if is_prime[i]:
        print(i)
