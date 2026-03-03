


vol_1 = {sym.strip() for sym in input().split()}
vol_2 = {sym.strip() for sym in input().split()}

vol_3 = vol_1 & vol_2

print(f'Уникальные руны первого свитка: {sorted(vol_1)}')
print(f'Уникальные руны второго свитка: {sorted(vol_2)}')
print(f'Защищённый свиток (общие руны): frozenset({sorted(vol_3)})')