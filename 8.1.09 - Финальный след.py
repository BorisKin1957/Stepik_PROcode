'''✅ Получить словарь (ключ = дата, значение = место).
✅ Удалить пробелы в местах (" Париж " → "Париж").
✅ Отсортировать по дате (по ключу словаря).
✅ Удалить повторяющиеся локации, но оставить первую встречу.
✅ Вывести финальный маршрут (Город → Город → Город).

Примечание: Не используйте set()!'''


from json import loads

data = loads(input())

data = dict(sorted(data.items(), key=lambda item: item[0]))

tour = {value.strip(): key for key, value in data.items()}

print(f"Маршрут: {' → '.join(tour.keys())}")





