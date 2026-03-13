'''Шаг 1. Объявите декоратор access_control(level), который принимает минимальный
уровень доступа.
Шаг 2. Декоратор должен оборачивать функцию и, основываясь на значении её параметра
user_level, поступать так:
– если уровень пользователя ниже требуемого → вернуть строку: Ошибка: доступ запрещен;
– если уровень достаточный → выполнить функцию и вернуть её результат.
Иерархия уровней: guest < manager < admin.
Шаг 3. Объявите функцию delete_data(user_level), которая имитирует удаление и при
успешном доступе возвращает строку:
✅ Данные успешно удалены (пользователь: <user_level>)
Шаг 4. Примените декоратор: @access_control('manager').'''


def access_control(required_level):
    # Задаём иерархию уровней
    levels = {'guest': 0, 'manager': 1, 'admin': 2}

    def decorator(func):
        def wrapper(user_level, *args, **kwargs):
            # Проверяем, существует ли уровень
            if user_level not in levels:
                return 'Ошибка: доступ запрещен'
            if required_level not in levels:
                return 'Ошибка: доступ запрещен'

            # Сравниваем уровни
            if levels[user_level]:
                return 'Ошибка: доступ запрещен'
            # Выполняем функцию
            return func(user_level, *args, **kwargs)

        return wrapper

    return decorator


@access_control('manager')
def delete_data(user_level):
    return f'✅ Данные успешно удалены (пользователь: {user_level})'


# Ввод уровня пользователя
name = input().strip()

# Вызов функции
print(delete_data(name))