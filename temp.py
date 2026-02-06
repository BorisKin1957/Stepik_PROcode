import re

password = input()

# Условие 1:
starts_with_letter = re.match(r'(?i)^[a-zа-я]', password)

# Условие 2 и 3:
valid_chars_and_length = re.match(r'^(?=.*[a-zA-Zа-яА-Я0-9])[a-zA-Zа-яА-Я0-9]{8,}$', password)

# Проверяем все условия
if starts_with_letter and valid_chars_and_length:
    print('Пароль принят!')
else:
    print('Пароль не принят!')