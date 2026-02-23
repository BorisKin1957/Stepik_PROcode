def get_book(string: str) -> dict:
    '''Возвращает словарь книги'''
    book = {}
    for item in string.split(', '):
        title, power = item.split(': ')
        book[title.strip()] = int(power.strip())

    return book

if get_book(input()) == get_book(input()):
    print('Книги идентичны')
else:
    print('Книги отличаются')