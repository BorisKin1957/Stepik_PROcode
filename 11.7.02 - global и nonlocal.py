'''Шаг 1. На уровне модуля объявите глобальную переменную security_level и присвойте
ей значение 0.
Шаг 2. Объявите функцию hack_system(), внутри которой:

    с помощью ключевого слова global измените security_level на 5;

    объявите локальную переменную defense_level и присвойте ей 0;

    объявите вложенную функцию defend_system(), в которой с помощью nonlocal измените
    defense_level на 10;

    вызовите defend_system();

    верните значение defense_level.
'''

# Глобальная переменная, доступная из любого места модуля
security_level = 0

def hack_system():
    # Указываем, что будем использовать глобальную переменную security_level
    global security_level
    security_level = 5  # Изменяем её значение на 5

    # Локальная переменная функции hack_system
    defense_level = 0

    def defend_system():
        # Указываем, что будем изменять переменную из внешней (но не глобальной) области — defense_level
        nonlocal defense_level
        defense_level = 10  # Меняем значение на 10

    # Вызываем вложенную функцию, чтобы изменить defense_level
    defend_system()

    # Возвращаем новое значение defense_level
    return defense_level

# В скрытых тестах будет выполнено примерно:
res = hack_system()
print(security_level)  # -> 5
print(res)             # -> 10