'''
✅ Объявить функцию analyze_text(text).
✅ Разбить строку на слова.
✅ Посчитать количество уникальных слов через множество.
✅ Вернуть:

    количество уникальных слов

    отсортированное множество в виде отсортированного списка.

'''

def analyze_text(string: str) -> tuple[int, list[str]]:
    result = set(string.split())
    return len(result), sorted(result)


print(analyze_text("бит стиль стиль бит ритм"))