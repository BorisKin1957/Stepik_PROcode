'''Пользователь вводит строку команд, разделённых пробелами.

Требуется:

    Преобразовать строку в список команд.
    Вывести сам список.
    Вывести количество всех команд.
    Вывести количество уникальных команд.
    Вывести команду, которая встречается чаще всего. Если таких несколько, вывести первую.

📌 Пример ввода:

MOVE JUMP WAIT MOVE SCAN MOVE ATTACK WAIT

📌 Пример вывода:

['MOVE', 'JUMP', 'WAIT', 'MOVE', 'SCAN', 'MOVE', 'ATTACK', 'WAIT']
Всего команд: 8
Уникальных команд: 5
Чаще всего используется: MOVE

'''


cmds = [cmd.strip() for cmd in input().split()]

unique = len(set(cmds))

frequent = max({cmd: cmds.count(cmd) for cmd in cmds}.items(), key=lambda x: x[1])[0]

print(cmds)
print(f'Всего команд: {len(cmds)}')
print(f'Уникальных команд: {unique}')
print(f'Чаще всего используется: {frequent}')