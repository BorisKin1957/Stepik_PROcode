

words = tuple(input().split())

unicum = []

for word in words:
    if word not in unicum:
        unicum.append(word)

print(len(unicum))
print(words)
