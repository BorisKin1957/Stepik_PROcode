


def convert_to_latin(text: str, sep: str = ' ') -> str:
    s = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
         'з': 'z',
         'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
         'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c',
         'ч': 'ch',
         'ш': 'sh', 'щ': 'shch', 'ы': 'y', 'э': 'e', 'ю': 'yu', 'я': 'ya', 'ё': 'yo'}

    result = []

    for word in text.split():
        trans = ''
        for letter in word:
            if letter.lower() in s:
                trans += s[letter.lower()]
            else:
                trans += letter
        result.append(trans)

    return sep.join(result)

string = input()
if (sym := input()):
    print(convert_to_latin(string, sym))
else:
    print(convert_to_latin(string))

