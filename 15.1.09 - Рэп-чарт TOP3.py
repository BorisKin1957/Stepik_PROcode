'''
✅ Прочитать количество рэперов.
✅ Ввести имя и баллы каждого.
✅ Сохранить пары в виде кортежей.
✅ Отсортировать список по убыванию баллов.
✅ Вывести топ-3.'''

chart = []

for _ in range(int(input())):
    lst = input().split()
    chart.append((' '.join(lst[:-1]), int(lst[-1])))

result = sorted(chart, key=lambda x: -x[1])[:3]

print(result)