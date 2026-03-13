'''Шаг 1. Объяви функцию send_command(a, b), которая возвращает сумму a + b. Ничего не печатает.
Шаг 2. Объяви декоратор log_command(func), который принимает функцию и возвращает обёртку.
Шаг 3. Обёртка должна принимать любые аргументы *args, **kwargs и работать так:
сначала печатает строку START <имя_функции>;
затем вызывает исходную функцию и получает результат;
затем печатает строку RESULT <результат>;
затем печатает строку END <имя_функции>;
после этого возвращает результат.
Шаг 4. Примени декоратор к функции с помощью @log_command.'''


def log_command(func):
    def wrapper(*args, **kwargs):
        print(f'START {func.__name__}')
        result = func(*args, **kwargs)
        print(f'RESULT {result}')
        print(f'END {func.__name__}')
        return result
    return wrapper



@log_command
def send_command(a: int, b: int) -> int:
    return a + b

send_command(3, 9)