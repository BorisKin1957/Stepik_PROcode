import re

with open('fragments.txt', 'r') as file:
    print(*re.findall(r'-?\d+', file.read()))