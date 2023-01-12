import zad


def is_internally_consistant(group):
    """
    sprawdza czy zbiór jest wewnętrznie spójny
    :param group:
    :return:
    """
    niepor = zad.get_niepor(group)
    por = {key: group[key] for key in group if key not in niepor}
    return bool(niepor), niepor, por


def is_externally_consistant(grater: dict, smaller: dict):
    """
    sprawdza czy zbiór grater dominuje zbiór smaller - zwraca dodatkowe wartości (na przyszłość)
    """
    bad = dict()
    true_sma = dict()
    not_eqeble = dict()
    for g in grater:
        for s in smaller:
            res = zad.is_domi(grater[g], smaller[s])
            if res == smaller[s]:
                bad.update({s: smaller[s]})
            elif res == grater[g]:
                true_sma.update({s: smaller[s]})
            elif res is None:
                not_eqeble.update({s: smaller[s]})
                bad.update({s: smaller[s]})

    consistancy = not bad
    if consistancy:
        return True, grater, smaller, dict(), not_eqeble
    else:
        return False, grater, true_sma, bad, not_eqeble









