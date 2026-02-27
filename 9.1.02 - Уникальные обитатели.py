

animals = input().split()
person = input()

print(f'Количество уникальных обитателей в Лесном Реестре: {len(set(animals))}')

print(f"Обитатель '{person}' зарегистрирован." if person in animals
      else f"Обитатель '{person}' не зарегистрирован.")