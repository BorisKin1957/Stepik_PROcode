

before = [int(input()) for _ in range(int(input()))]
after = before[-1:] + before[:-1]

print(f'Исходный кортеж: {tuple(before)}')
print(f'Кортеж после сдвига: {tuple(after)}')