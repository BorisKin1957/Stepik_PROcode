


group_1 = {name.strip() for name in input().split()}
group_2 = {name.strip() for name in input().split()}

print(f'Все мастера входят в первое множество: {group_2.issubset(group_1)}')