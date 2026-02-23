

string = input().split(', ')

magic_keys = {}

for item in string:
    number, key = item.split(': ')
    magic_keys[int(number)] = key

print(f'Сумма всех ключей: {sum(magic_keys)}')
print(f'Минимальный ключ: {min(magic_keys)}')
print(f'Максимальный ключ: {max(magic_keys)}')