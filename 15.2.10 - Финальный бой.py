'''
🎯 Задание:

Напиши функцию fight_boss(attacks, boss_defense), которая принимает:

    attacks -- список словарей, каждый из которых описывает атаку:
        {"name": str, "power": int, "type": str}

    boss_defense — словарь, содержащий параметры босса:
        "armor": int — защита (снижает урон),
        "weakness": str — тип атаки, на который Босс уязвим (твой бонус),
        "shield": int — щит (дополнительно уменьшает урон).

Функция должна:

    Выбрать атаку, которая наносит наибольший урон с учётом бонусов:
        Если attack["type"] == boss["weakness"], к attack["power"] прибавляется +50% (округляется вверх).
    Отнять урон Босса armor + shield и вернуть:
        Название лучшей атаки.
        Урон после всех защит (не меньше нуля).
        Сообщение "Победа!", если урон > 100, иначе — "Босс выжил...".

📌 Пример вызова 1:

attacks = [
    {"name": "Огненный удар", "power": 80, "type": "огонь"},
    {"name": "Ледяная стрела", "power": 60, "type": "лед"},
    {"name": "Теневая вспышка", "power": 90, "type": "тьма"}
]

boss = {
    "armor": 30,
    "shield": 20,
    "weakness": "огонь"
}

print(fight_boss(attacks, boss))


📌 Ожидаемый вывод:

('Огненный удар', 70, 'Босс выжил...')
'''

import math


def fight_boss(attacks, boss_defense):
    best_attack = None
    max_damage = -1

    for attack in attacks:
        power = attack["power"]
        # Применяем бонус, если тип атаки соответствует слабости босса
        if attack["type"] == boss_defense["weakness"]:
            power = math.ceil(power * 1.5)  # +50%, округление вверх

        # Рассчитываем урон после защиты
        total_damage = power - boss_defense["armor"] - boss_defense["shield"]
        total_damage = max(0, total_damage)  # Урон не может быть меньше нуля

        # Выбираем атаку с максимальным уроном
        if total_damage > max_damage:
            max_damage = total_damage
            best_attack = attack["name"]

    # Определяем результат боя
    result_message = "Победа!" if max_damage > 100 else "Босс выжил..."

    return (best_attack, max_damage, result_message)


attacks = [
    {"name": "Пылающий шторм", "power": 100, "type": "огонь"},
    {"name": "Копьё молнии", "power": 90, "type": "электричество"},
    {"name": "Магма", "power": 95, "type": "огонь"}
]

boss = {
    "armor": 20,
    "shield": 10,
    "weakness": "огонь"
}

print(fight_boss(attacks, boss))