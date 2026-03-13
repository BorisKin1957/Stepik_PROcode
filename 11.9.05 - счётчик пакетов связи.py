'''Шаг 1. Объяви декоратор count_calls(func), который принимает функцию и возвращает
обёртку wrapper.
Шаг 2. Декоратор должен хранить счётчик вызовов в замыкании и увеличивать его при
каждом вызове обёртки.
Шаг 3. Обёртка должна принимать *args, **kwargs, вызывать исходную функцию и возвращать
кортеж (результат, номер_вызова).
Шаг 4. Объяви функцию encode(text), которая возвращает строку text в нижнем регистре.
Ничего не печатает.
Шаг 5. Примени декоратор к функции с помощью @count_calls.'''

def count_calls(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        result = func(*args, **kwargs)
        return result, count

    return wrapper


@count_calls
def encode(text: str) -> str:
    return text.lower()


print(encode('qwert'))
print(encode('qwert'))