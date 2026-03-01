

# Начальный список участников
participants = {1, 2, 3, 4, 5}

for num in map(int, input().split()):
    participants.add(num)

print(f'После добавления участников: {participants}')

if (num := int(input())) in participants:
    participants.remove(num)
print(f'После удаления участника с номером {num}: {participants}')

participants.discard(num := int(input()))
print(f'После удаления участника с номером {num} (метод discard): {participants}')

num = participants.pop()
print(f'Удалён случайный участник с номером {num}.')

print(f'Оставшиеся участники: {participants}')

participants.clear()
print(f'После очистки списка участников: {participants}')