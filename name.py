def my_name(viborka, name):
    if name in viborka:
        return True
    else:
        return False


viborka = ["Валерия", "Лера"]

name = input("Введите имя:")
result = my_name(viborka, name)
if result:
    print("Это ж я")
else:
    print(f"Hello, {name}")
