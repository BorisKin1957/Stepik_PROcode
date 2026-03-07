def func(lst, *args):
    for arg in args:
        if arg not in lst:
            lst.append(arg)
    return lst

scrolls = input().split()
relics = input().split()

artifact_collection = func(scrolls, *relics)

print(*artifact_collection)