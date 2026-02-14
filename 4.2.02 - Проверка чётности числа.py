'''Создайте функцию check_parity(number), которая принимает одно число и возвращает строку:

    четное --> если число чётное;
    нечетное --> если число нечётное.
'''


def check_parity(number: int) -> str:
    return 'нечетное' if number % 2 else 'четное'


print(check_parity(int(input())))
