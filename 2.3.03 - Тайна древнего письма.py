

rev = input()[::-1]

result = ''

for sym in rev:
    if sym.isalnum():
        result += sym

print('Тайна разгадана' if result.upper() == result.upper()[::-1] else 'Тайна не разгадана')



