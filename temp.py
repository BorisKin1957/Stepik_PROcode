ввод = input()

# Разделение строки на элементы по пробелам
элементы = ввод.split()

# Обработка каждого элемента
for элемент in элементы:
    if элемент.startswith('"') and элемент.endswith('"') and len(элемент) >= 2:
        print("str")
    elif элемент == "True" or элемент == "False":
        print("bool")
    else:
        if '.' in элемент:
            try:
                float(элемент)
                print("float")
            except ValueError:
                print("Неверный тип данных")
        else:
            try:
                int(элемент)
                print("int")
            except ValueError:
                print("Неверный тип данных")