# пароли
old_passwords = ('virus', 'antivirus', 'zombie', 'virus', 'bio', 'zombie', 'bio', 'virus',
'biohazard', 'virus', 'biohazard')

tmp = list(old_passwords)
tmp.extend([input() for _ in range(2)])

new_passwords = []

for word in tmp:
    if word not in new_passwords:
        new_passwords.append(word)

new_passwords.sort(key=len)
new_passwords = tuple(new_passwords)

print(f'Старый кортеж паролей: {old_passwords}')
print(f'Новый кортеж паролей: {new_passwords}')