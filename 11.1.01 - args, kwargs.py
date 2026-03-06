

def filter_magic_numbers(*args):
    return [num for num in args if num % 2 == 0]

print(*filter_magic_numbers(*[int(num) for num in input().split()]))