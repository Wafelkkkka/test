import math

temp = input("Введите температуру в C или в F:")

if temp.endswith("C"):  # Если температура введена в Цельсиях
    temp_c = float(temp[:-1])  # Извлекаем числовое значение
    temp_f = temp_c * 5 / 9 + 32  # Переводим в Фаренгейты
    print(f"{temp_f} F")
elif temp.endswith("F"):  # Если температура введена в Фаренгейтах
    temp_f = float(temp[:-1])  # Извлекаем
    temp_c = (temp_f - 32) * 5 / 9  # переводим в C
    print(f"{temp_c} C")
else:
    print("Неверный ввод! Используйте 'C' или 'F'. Например: 40C или 100F")
