


# данные лошадей
horses = (("Буря", 48), ("Черный ворон", 44), ("Молния", 60))

name, way = input(), int(input())
flag = False

for horse, speed in horses:
    if name == horse:
        full_time = way / speed
        hours = int(full_time)
        minutes = round((full_time - hours) * 60)
        flag = True

if flag:
    print(f'Лошадь {name} пройдет {way} км за {hours} часов и {minutes} минут.')
else:
    print('Лошадь с таким именем не найдена.')


