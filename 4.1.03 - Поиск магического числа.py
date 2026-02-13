
def get_one_number(numbers: list[int]) -> int:
    '''Выводит число кратное 7'''
    for number in numbers:
        if number % 7 == 0:
            return number


print(get_one_number(map(int, input().split())))