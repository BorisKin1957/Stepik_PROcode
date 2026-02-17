

# кортеж с данными о магических городах
cities = ('Эльдорадо', 'Люминор', 'Арканум')
populations = (5000, 7000, 12000)
magics = ('Земная магия', 'Воздушная магия', 'Водная магия')

cities = cities + (input(),)
populations = populations + (int(input()),)
magics = magics + (input(),)

print(cities, populations, magics, sep='\n')