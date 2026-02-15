


def calculate_platform(length, width, mode=0):
    return 2 * (length + width) if mode == 0 else length * width


print(calculate_platform(140, 100))