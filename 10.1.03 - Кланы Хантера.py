

hunters = {name.strip() for name in input().split()}
criminals = {name.strip() for name in input().split()}


print(f'Общие: {{{', '.join(sorted(hunters & criminals))}}}')
print(f'Чистые охотники: {{{', '.join(sorted(hunters - criminals))}}}')