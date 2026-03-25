

import json

data = json.loads(input())

print(f'Артефакт {data['id']} содержит {len(data['components'])} компонента(ов).')
print(json.dumps(data, indent=4))

with open('artifact.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)