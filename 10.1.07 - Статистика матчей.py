


actions_1 = {action.strip() for action in input().split(',')}
actions_2 = {action.strip() for action in input().split(',')}

print(f'Общие достижения: {sorted(actions_1.intersection(actions_2))}')
print(f'Достижения только в матче 1: {sorted(actions_1 - actions_2)}')
print(f'Достижения только в матче 2: {sorted(actions_2 - actions_1)}')