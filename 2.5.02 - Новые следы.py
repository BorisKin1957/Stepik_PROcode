

signals = input().split(', ')
count = 0

while signals:
    if signals.pop() == 'ignore':
        print('ignore')
        count += 1
print(count)