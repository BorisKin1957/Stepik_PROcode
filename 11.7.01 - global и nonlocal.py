'''Шаг 1. В программе уже задана функция initialize_data() с вложенной функцией update_data().
Шаг 2. Отредактируйте код так, чтобы переменная username, объявленная в initialize_data(),
изменялась внутри update_data().
Шаг 3. После запуска программа должна вывести обновлённое имя пользователя дважды:
— один раз внутри update_data() (там уже есть print),
— второй раз после вызова update_data() в initialize_data() (там тоже уже есть print).

Ограничения:
– Не меняйте имена функций и переменной username.
– Формат ввода/вывода должен совпадать с примером.'''

def initialize_data():
    username = input()

    def update_data():
        nonlocal username       # только это добавил в код
        username = input()
        print(username)

    update_data()
    print(username)

initialize_data()