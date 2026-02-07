
power, experience = int(input()), int(input())

# if power < 50:
#     print('Выберите меч!')
# elif 50 <= power <= 100 and experience < 20:
#     print('Выберите лук и стрелы!')
# elif 50 <= power <= 100 and experience >= 20:
#     print('Выберите магический посох!')
# else:
#     print('Выберите любое оружие на ваш выбор!')

if power < 50:
    print('Выберите меч!')
elif 50 <= power <= 100:
    print('Выберите магический посох!' if experience >= 20 else 'Выберите лук и стрелы!')
else:
    print('Выберите любое оружие на ваш выбор!')