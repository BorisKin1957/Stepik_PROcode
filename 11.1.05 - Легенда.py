

def lex_min(a: str, b: str) -> str:
    return min(a, b)


def lex_min3(a: str, b: str, c: str) -> str:
    return min(lex_min(a, b), c)


def lex_min4(a: str, b: str, c: str, d: str) -> str:
    return min(lex_min3(a, b, c), d)



