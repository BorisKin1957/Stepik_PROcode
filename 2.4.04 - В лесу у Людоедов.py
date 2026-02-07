# from unittest import case

time, answer = input(), input()

match time:
    case 'день':
        print('Людоеды съели вас.' if answer == 'да'
              else 'Вы прошли в деревню.')
    case 'ночь':
        print('Людоеды поймали вас.' if answer == 'да'
              else 'Вы прошли в деревню.')
    case _:
        print('Не корректный ввод данных')