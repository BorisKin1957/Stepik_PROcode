

def calculate_platform(length, width, mode=0):
    return length * width if mode else 2 * (length + width)

print(calculate_platform(140, 100, 6))