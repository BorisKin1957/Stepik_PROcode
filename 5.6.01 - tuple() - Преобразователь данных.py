

# кортеж паролей
old_passwords = ('qwerty', '123456', 'abc123')

new_passwords = list(old_passwords)
new_passwords.append(input())

print(f'Старый кортеж: {old_passwords}')
print(f'Новый кортеж: {tuple(new_passwords)}')
