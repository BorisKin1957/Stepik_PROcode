


def create_initials(name: str, surname: str, patronymic: str) -> str:
    '''вывести (через print) инициалы'''
    print(surname[0].upper() + name[0].upper() + patronymic[0].upper())


name, surname, patronymic = input(), input(), input()

create_initials(name, surname, patronymic)