'''
✅ Получить число фанатов.
✅ Затем построчно ввести имя и любимый трек.
✅ Сохранить пары в словарь.
✅ Вывести словарь.
'''

result = {}

for _ in range(int(input())):
    s = input().split()
    result[s[0]] = result.get(s[0], ' '.join(s[1:]))

print(result)