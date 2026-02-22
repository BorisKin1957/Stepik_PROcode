


# кортеж книг
old_books = (
    'Мастер и Маргарита',
    'Война и мир',
    '1984',
    'Преступление и наказание',
    '451 градус по Фаренгейту',
    '1984'
)

add_books = input().split(', ')
add_books = [book.strip() for book in add_books]

tmp_books = list(old_books)
tmp_books.extend(add_books)
new_books = []

for book in tmp_books:
    if book not in new_books:
        new_books.append(book)

new_books = tuple(sorted(new_books))

print(f'Исходный кортеж книг: {old_books}')
print(f'Новый кортеж книг: {new_books}')

