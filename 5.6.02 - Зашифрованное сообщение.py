


# сообщение
message_tuple = ('Агент', 'Джей,', 'твоя', 'следующая', 'миссия')

word = input()

full_message = ' '.join((message_tuple + (word,)))

print(f'Исходное сообщение: {message_tuple}')
print(f'Полное сообщение: {full_message}')
