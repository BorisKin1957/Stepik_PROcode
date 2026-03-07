

core_data = list(map(int, input().split()))
signal1, signal2, signal3, signal4 = core_data[5:-1]
activation_code = core_data[-1]

print(*core_data[:5])