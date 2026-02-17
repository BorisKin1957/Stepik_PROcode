


# кортеж с именами бандитов
bandits = ("Vitorio Zanzara", "Джек", "Dagdarion Dark", "Артур", "Алекс Глозман", "Рик", "Dark Horse")

print(f'{name} в сборе!' if (name := input()) in bandits else f'{name} не найден в списке!')