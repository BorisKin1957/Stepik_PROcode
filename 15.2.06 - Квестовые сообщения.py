'''Пользователь вводит сообщение (строку). Нужно:

    Привести текст к нижнему регистру и разбить на слова.
    Найти и вывести три самых частых слова с числом повторов.
    Если слов меньше трёх, вывести столько, сколько есть.
    Слова сортировать по убыванию частоты, при равенстве -- по алфавиту.
'''



from collections import Counter

words = [word.strip().lower() for word in input().split()]

result = sorted(Counter(words).items(), key=lambda x: (-x[1], x[0]))
result = result[:3] if len(result) > 2 else result

for item in result:
        print(*item)