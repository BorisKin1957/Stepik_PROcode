

group_1 = set(name.strip() for name in input().split(','))
group_2 = set(name.strip() for name in input().split(','))

if group_1 & group_2:
    if group_1.issubset(group_2):
        print('Первая группа - подмножество второй.')
    elif group_2.issubset(group_1):
        print('Вторая группа - подмножество первой.')
    else:
        print('Группы пересекаются, но ни одна не является подмножеством другой.')
else:
    print('Группы не пересекаются.')