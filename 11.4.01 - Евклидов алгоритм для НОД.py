def euclid_gcd_iterative(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a, b = int(input()), int(input())

print(f'Наибольший общий делитель чисел равен: {euclid_gcd_iterative(a, b)}')
