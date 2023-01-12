from copy import deepcopy
from math import inf

from numpy import vstack


def apply_maxim(matrix, vector):
    """
    za pomocą wektora vector można określić które
    kryteria mają być maksymalizowane a które minimalizowane
    1 - maksymalizacja kryterium
    0 - minimalizacja kryterium
    """
    v2 = [1 if x == 0 else -1 for x in vector]
    # v2 1 1 -1
    matrix = matrix * v2
    matrix = matrix + vector
    # matrix a b c -> a 1-b 1-c
    return matrix


def print_rank(rank):
    """
    wyprintowanie wyniku
    """
    print(*rank, sep='\n')


def sort_res(ci):
    """
    posortowanie wyniku
    """
    inp = list(enumerate(ci, 1))
    return sorted(inp, key=lambda x: x[1], reverse=True)


def normalize(matrix):
    """
    normalizacja macierzy
    """
    matrix = matrix / ((matrix ** 2).sum(axis=0)) ** (1/2)
    return matrix


def get_dig(matrix, mat_min):
    """
    obliczenie parametru dg
    """
    matrix = matrix - mat_min
    matrix = matrix ** 2
    return sum(matrix.T)


def get_did(matrix, mat_max):
    """
    obliczenie parametru dd
    """
    matrix = matrix - mat_max
    matrix = matrix ** 2
    return sum(matrix.T)


def get_ci(dig, did):
    """
    obliczenie parametru ci
    """
    return did / (did + dig)


def is_domi(x, y):
    """
    funkcja sprawdzająca czy dany punkt dominuje drugi
    :param x: pkt 1
    :param y: pkt 2
    :return: x,y - większy, None - nieporównywalne, Err - takie same
    """
    gr = [None] * 3
    eq = deepcopy(gr)
    sm = deepcopy(gr)

    for i in range(len(x)):
        gr[i] = (x[i] >= y[i])
        eq[i] = (x[i] == y[i])
        sm[i] = (x[i] <= y[i])
    if all(eq):
        raise ValueError(f"the same error {x}")  # dwa takie same punkty
    if all(gr):
        return x  # punkt x większy
    elif all(sm):
        return y  # punkt y większy
    else:
        return None  # punkty nieporównywalne


def get_rest(b, niezdom_dod, niezdom_uj):
    """
    Funkcja zwracająca resztę z danego zbioru b - (niezdom_dod + niezdom_uj)
    :param b:
    :param niezdom_dod:
    :param niezdom_uj:
    """
    return {key: val for key, val in b.items() if key not in niezdom_dod and key not in niezdom_uj}


def is_niepor(b):
    """
    funkcja zwraca punktu nieporównywalne z danego zbioru
    :param b: zbiór
    """
    niepor = dict()
    for pkt in b:
        for pkt2 in b:
            if b[pkt] != b[pkt2]:
                res = is_domi(b[pkt], b[pkt2])
                if res:
                    break
        else:
            niepor.update({pkt: b[pkt]})
    return niepor


def repr_reslt(rest, dod, uj):
    """
    prezentacja wyiku
    """
    print("NIEZDOM DOD:")
    str_repr(dod)
    print("NIEZDOM  UJ:")
    str_repr(uj)
    print("REST:")
    str_repr(rest)


def get_niezdom(b):
    """
    funkcja wyciąga z danego zbioru punkty niezdominowane dodatnio, niezdominowane ujemnie i nieporównywalne
    :param b: zbiór
    :return:
    """
    niezdom_dod = deepcopy(b)
    niezdom_uj = deepcopy(b)
    niepor = get_niepor(b)
    for pkt in b:
        for pkt2 in b:
            if b[pkt] != b[pkt2]:
                res = is_domi(b[pkt], b[pkt2])
                if res == b[pkt2]:
                    niezdom_dod.pop(pkt, None)
                    niezdom_uj.pop(pkt2, None)
                if res == b[pkt]:
                    niezdom_dod.pop(pkt2, None)
                    niezdom_uj.pop(pkt, None)

    niezdom_dod = get_rest(niezdom_dod, niepor, dict())
    niezdom_uj = get_rest(niezdom_uj, niepor, dict())
    return niezdom_dod, niezdom_uj, niepor





def str_repr(struct):
    for x in struct:
        print(x, struct[x], sep=' ')


def get_max_min(struct):
    """
    funkcja zwraca najmniejszy i największy element
     struktury (nie koniecznie do niej należący)
    """
    min_ = [inf] * 3
    max_ = [-inf] * 3
    for val in struct.values():
        for i in (0, 1, 2):
            min_[i] = min(min_[i], val[i])
            max_[i] = max(max_[i], val[i])
    return {"MIN": min_, "MAX": max_}


def dic2matrix(dict_):
    """
    zamiana słownika na macierz numpy
    """
    keys = list(dict_.keys())
    arr = dict_[keys[0]]
    for key in keys[1:]:
        arr = vstack([arr, dict_[key]])
    return arr, keys


def chyb_metr(matrix, max_, min_):
    """
    metryka czybyszewa dla macierzy z zadanymi max i min
    """
    max_odl = max_-matrix
    min_odl = matrix-min_
    return min_odl, max_odl


def eukl_metr(matrix, max_, min_):
    """
    metryka euklidesowa dla macierzy z zadanymi max i min
    """
    max_odl = (max_ - matrix) ** 2
    min_odl = (matrix - min_) ** 2
    return min_odl, max_odl


def my_metr(matrix, max_, min_):
    """
    nasza metryka dla macierzy z zadanymi max i min
    """
    max_odl = abs(max_ - matrix) ** (1/2)
    min_odl = abs(matrix - min_) ** (1/2)
    return min_odl, max_odl


def get_did_2(matrix, metr, min_, max_):
    """
    zwraca parametry did i dig dla metody fuzzy topsis z zadanymi punktami min i max
    """
    dig_alm, did_alm = metr(matrix, max_, min_)
    dig = sum(dig_alm.T)
    did = sum(did_alm.T)
    return dig, did


def sort_res_2(ci, keys):
    inp = list(zip(keys, ci))
    return sorted(inp, key=lambda x: x[1], reverse=True)


def topsis2(matrix, min_, max_, metr, keys, vector):
    """
    funkcja obliczająca fuzzy topsis dla danej macierzy
     z zadaną metryką i wartościami max i min
    """
    matrix = normalize(matrix)
    matrix = apply_maxim(matrix, vector)
    dig, did = get_did_2(matrix, metr,  min_, max_)
    ci = get_ci(dig, did)
    rank = sort_res_2(ci, keys)
    print_rank(rank)


data = {'M1': [58000.0, 1.0, 7.0], 'M2': [120000.0, 3.2, 8.0], 'M3': [80000.0, 4.8, 5.0], 'M4': [68000.0, 1.6, 6.0],
     'M5': [12000.0, 0.9, 3.0], 'M6': [16000.0, 1.9, 5.0], 'M7': [102000.0, 2.4, 8.0],
     'M8': [298000.0, 4.2, 10.0], 'M9': [79000.0, 1.9, 7.0], 'M10': [62000.0, 2.0, 6.0], 'M11': [19000.0, 1.2, 5.0],
     'M12': [14000.0, 1.4, 3.0], 'M13': [9000.0, 1.6, 2.0], 'M14': [5000.0, 1.9, 2.0], 'M15': [229000.0, 3.0, 9.0],
     'M16': [71000.0, 2.4, 6.0], 'M17': [81000.0, 2.0, 9.0], 'M18': [34000.0, 1.9, 6.0], 'M19': [41000.0, 5.0, 4.0],
     'M20': [102000.0, 4.0, 7.0], 'M21': [20000.0, 2.8, 3.0], 'M22': [64000.0, 6.2, 5.0],
     'M23': [54000.0, 1.8, 6.0], 'M24': [167000.0, 3.6, 8.0], 'M25': [99000.0, 4.2, 5.0],
     'M26': [38000.0, 1.4, 7.0], 'M27': [47000.0, 1.2, 9.0], 'M28': [24000.0, 0.9, 6.0],
     'M29': [66000.0, 1.8, 8.0], 'M30': [18000.0, 1.0, 6.0]}


if __name__ == "__main__":
    """
    główny kod programu FUZZY TOPSIS
    """
    print('\n---ITERACJA 1---\n')
    print("A0, A3")
    niezdom_dod, niezdom_uj, nie_por = get_niezdom(data)
    data_rest = get_rest(data, niezdom_dod, niezdom_uj)
    # co z nieporównywalnym
    repr_reslt(data_rest, niezdom_dod, niezdom_uj)
    print("Nieporównywalne:")
    str_repr(nie_por)
    glob_max_min = get_max_min(data)
    print(glob_max_min)
    print('\n---ITERACJA 2---\n')

    print("A1, A2")
    niezdom_dod_2, niezdom_uj_2, nie_por_2 = get_niezdom(data_rest)
    rest_2 = get_rest(data_rest, niezdom_dod_2, niezdom_uj_2)
    # co z nieporównywalnym
    repr_reslt(rest_2, niezdom_dod_2, niezdom_uj_2)
    print("Nieporównywalne:")
    str_repr(nie_por_2)
    loc_max_min = get_max_min(data_rest)
    print(loc_max_min)
    print('\n---KONIEC ITERACJI---\n')

    matrix_fuzzy, keys_fuzzy = dic2matrix(rest_2)

    methods = (chyb_metr, my_metr, eukl_metr)
    names = ("chyb_metr", "my_metr", "eukl_metr")
    vector = [0, 0, 0]


    for method, m_name in zip(methods, names):
        print("\n-------------- metric: ", m_name)
        print("\n---- normal topsis:")
        topsis2(matrix_fuzzy, glob_max_min["MIN"], glob_max_min["MAX"], method, keys_fuzzy, vector)

        print("\n---- fuzzy topsis")
        topsis2(matrix_fuzzy, loc_max_min["MIN"], loc_max_min["MAX"], method, keys_fuzzy, vector)
        print("------------------------------------")



