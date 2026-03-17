


def check_systems(*args: list):
    print('Проверка систем:')
    for arg in args:
        print(f'- {arg}: OK')


systems = [system.strip() for system in input().split(',')]
check_systems(*systems)