def access_control(level):
    def decor(f):
        def wrap(a):
            if user_level not in ['manager', 'admin']:
                return 'Ошибка: доступ запрещен'
            return f(a)

        return wrap

    return decor


@access_control('')
def delete_data(user_level):
    return f'✅ Данные успешно удалены (пользователь: {user_level})'

# Ввод уровня пользователя
user_level = input().strip()

# Вызов функции
print(delete_data(user_level))