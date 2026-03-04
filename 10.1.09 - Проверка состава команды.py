

all_merits = {merit.strip() for merit in input().split(',')}
players = []

for _ in range(int(input())):
    tmp = input().split(':')
    any_merits = {merit.strip() for merit in tmp[1].split(',')}
    if any_merits.issuperset(all_merits):
        players.append(tmp[0])

if players:
    print(f'Игроки с полным набором навыков: {', '.join(players)}')
else:
    print('Нет игроков с полным набором навыков')
