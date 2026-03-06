


def order_summary(*orders, main_order: str) -> dict:
    result = {'orders': []}
    for order in orders:
        result['orders'].append(order)
    result['main_order'] = main_order
    return result

print(order_summary('Пицца', 'Бургер', 'Картофель фри', main_order='Сет №5'))