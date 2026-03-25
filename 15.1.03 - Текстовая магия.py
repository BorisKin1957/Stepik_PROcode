


# result = {}
#
# for word in input().split():
#     result[word] = result.get(word, 0) + 1

txt = input().split()

print({word: txt.count(word) for word in txt})