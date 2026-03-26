

def analyze_portals(portal_list):
    lst = sorted(portal_list)
    avg = sum(lst) / len(lst)
    st = set(num for num in lst if num > avg)

    return lst, st





print(analyze_portals([80, 120, 50, 200, 90]))