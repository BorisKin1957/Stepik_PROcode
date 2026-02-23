ants = [{'name': 'Eva', 'phone': '112-342-6711', 'email': 'eva.smith@mail.com'},
        {'name': 'Milo', 'phone': '555-982-6741', 'email': 'milo.james@outlook.com'},
        {'name': 'Sophia', 'phone': '478-245-8912', 'email': ''},
        {'name': 'Theo', 'phone': '555-673-8345', 'email': 'theo.green@protonmail.com'},
        {'name': 'Viktor', 'phone': '417-145-2031', 'email': 'viktor.kaplan@mail.ru'},
        {'name': 'Liam', 'phone': '321-452-7391', 'email': ''},
        {'name': 'Chloe', 'phone': '+7996-789-1234', 'email': 'chloe.miller@icloud.com'},
        {'name': 'Zoe', 'phone': '+7916-542-3124', 'email': 'zoe.williams@gmail.com'},
        {'name': 'David', 'phone': '411-568-9971', 'email': ''},
        {'name': 'Omar', 'phone': '178-903-4768', 'email': 'omar.zahid@outlook.com'},
        {'name': 'Igor', 'phone': '+7956-234-9876', 'email': 'igor.ivanov@mail.com'},
        {'name': 'Kira', 'phone': '7356-478-9201', 'email': ''},
        {'name': 'Leo', 'phone': '+7423-167-2091', 'email': 'leo.pratt@mail.ru'},
        {'name': 'Anna', 'phone': '15-674-3912', 'email': 'anna.morrison@tutanota.com'},
        {'name': 'Max', 'phone': '+7534-287-0654', 'email': ''},
        {'name': 'Charlie', 'phone': '253-346-7024', 'email': 'charlie.jones@gmail.com'}]

result = [ant['name'] for ant in ants if ant['phone'].endswith('1')]

result.sort(key=str.lower)

print(*result)

