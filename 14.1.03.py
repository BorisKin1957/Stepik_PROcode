

# Читаем имя файла из ввода
filename = input().strip()

# далее ваш код
with open(filename, 'r', encoding='utf-8') as f:
    count = 0
    for line in f.readlines():
        print(line.strip())
        count += 1
    print(count)