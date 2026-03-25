'''
✅ Объявить функцию find_max_line().
✅ Внутри пройтись по строкам и найти ту, где больше всего слов. Если таких несколько, вернуть первую.
✅ Вернуть эту строку.
'''

def find_max_line(words: [list[str]]) -> str:
    '''Вернет самую многословную строку списка'''
    return max(words, key=lambda x: len(x.split()))


lst = []
while (s := input()) != 'END':
    lst.append(s)

print(find_max_line(lst))