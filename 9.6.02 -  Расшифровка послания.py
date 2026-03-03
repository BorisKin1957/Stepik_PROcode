

string = input()

digits = {int(sym) for sym in string if sym.isdigit()}
letters = {letter for letter in string if letter.isalpha()}

print(f'Уникальные цифры: {{{', '.join(map(str, sorted(digits)))}}}')
print(f'Уникальные буквы: {{{', '.join(sorted(letters))}}}')