


def can_form_triangle(a: int, b: int, c: int) -> bool:
    '''из этих сторон можно составить треугольник?'''
    return a + b > c and a + c > b and b + c > a


print(can_form_triangle(1, 2, 3))
print(can_form_triangle(5, 7, 10))