# Считываем список показателей из отчёта (через запятую)
report_stats = set(input().split(', '))

# Считываем frozenset лучших показателей (через запятую)
best_stats = frozenset(input().split(', '))

found_best = set(report_stats & best_stats)
missing_best = set(best_stats - report_stats)
extra_stats = set(report_stats - best_stats)

print(f'Найденные лучшие показатели {found_best}')
print(f'Отсутствующие лучшие показатели: {missing_best}')
print(f'Лишние показатели в отчёте: {extra_stats}')