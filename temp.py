n = tuple(
    map(int, input().replace(') ', ', ').replace('(', '').replace(')', '').split(', ')))
i, nn = 0, []

while i < len(n):
    nn.append((n[i], n[i + 1]))
    i += 2
nn = tuple(nn)

print(f"""Кортеж с минимальным первым элементом: {min(nn)}
Кортеж с максимальным первым элементом: {max(nn)}""")