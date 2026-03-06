

def political_debate(*arguments, key_argument):
    print('🗣 Политические дебаты начинаются!\n📢 Политики приводят доводы:')
    for arg in arguments:
        print(f'- {arg}')
    print(f'🔥 Ключевой аргумент: {key_argument}\n✅ Дебаты завершены!')
