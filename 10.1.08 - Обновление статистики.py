

actions = {action.strip() for action in input().split(',')}

add = {action.strip() for action in input().split(',')}
actions |= add

excess = {action.strip() for action in input().split(',')}
actions -= excess

print(f'{{{', '.join(sorted(actions))}}}')
