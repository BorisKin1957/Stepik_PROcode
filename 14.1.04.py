

with open('ancient_key.txt', 'r') as f:
    print(sum([int(line) for line in f.readlines()]))