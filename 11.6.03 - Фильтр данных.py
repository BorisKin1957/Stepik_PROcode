'''Шаг 1. Объявите внешнюю функцию data_converter(tp), где tp --> строка "list" или "tuple".
Шаг 2. Внутри неё создайте и верните вложенную функцию, которая принимает одну строку
с числами, разделёнными пробелами.
Шаг 3. Вложенная функция должна преобразовать строку в последовательность целых чисел и вернуть:

    list[int], если tp == "list";

    tuple[int, ...], если tp == "tuple".
'''

def data_converter(tp):
    def inner(string):
        result = [int(num) for num in string.split()]
        return result if tp == 'list' else tuple(result)
    return inner

#Пример использования
# func = data_converter('list')
# text = '1 2 3 4 5'
#
# print(func(text))