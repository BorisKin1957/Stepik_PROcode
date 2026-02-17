

# кортеж с именами бандитов
bandits = ("Vitorio Zanzara", "Джек", "Dagdarion Dark", "Артур", "Алекс Глозман", "Рик", "Dark Horse")

print(f'Каждый бандит получит: {spoil // len(bandits)} монет.'
      if (spoil := int(input())) % len(bandits) == 0
      else 'Общая сумма добычи не делится поровну между бандитами.')