mage_health = 20
bro_health = 20

while mage_health > 0 and bro_health > 0:
    if input().strip() == 'простая атака':
        bro_health -= 4
    else:
        mage_health -= 2
        bro_health -= 6
    if input().strip() == 'атака':
        mage_health -= 5
    else:
        mage_health -= 3
        bro_health += 2
    if 0 < mage_health < 4:
        mage_health += 5
    print(f'Жизни Мага: {mage_health}')
    print(f'Жизни братьев: {bro_health}')

print('Магия победила, и ваши души теперь мои!' if mage_health > bro_health
      else 'Знаешь, что хуже магии? Братья Маузеры с оружием в руках.')