


sinners = {name.strip() for name in input().split()}
name = input().strip()

sinners.add(input().strip())

if name in sinners:
    sinners.remove(name)

print(f'{{{', '.join(sorted(sinners))}}}')