

import sys

lst = list(map(str.strip, sys.stdin.readlines()))

print(len(set(lst)))