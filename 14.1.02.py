
# Читаем имя файла из ввода
filename = input().strip()

# далее ваш код
with open(filename, 'r', encoding='utf-8') as file:
    print(file.read())
    file.seek(0)
    print(file.readline().strip())