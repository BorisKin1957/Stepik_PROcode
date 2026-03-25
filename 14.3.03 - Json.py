
import json

data = {}

data['mission'] = input()
status = True if input() == 'True' else False
data['success'] = status
data['samples'] = input().split(', ')
data['duration'] = int(input())

print(json.dumps(data, indent=4))

with open('report.json', 'w') as file:
    json.dump(data, file, indent=4)  # Записываем данные в файл


