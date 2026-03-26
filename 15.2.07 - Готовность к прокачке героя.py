

def analyze_exp(exp_list: list[int]) -> dict:
    maximum = max(exp_list)
    minimum = min(exp_list)
    summa = sum(exp_list)
    battles = len(exp_list)
    avg = round(summa / battles)
    level_up = True if summa > 500 else False
    return {
        'max': maximum,
        'min': minimum,
        'sum': summa,
        'avg': avg,
        'battles': battles,
        'level_up': level_up,
         }




print(analyze_exp([120, 130, 150, 90, 110]))