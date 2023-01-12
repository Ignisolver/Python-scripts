from numpy import array as arr
from pandas import read_csv


def import_data(path):
    """
    pobranie danych z pliku csv
    """
    matrix = read_csv(path)
    return matrix.to_numpy()


def normalize(matrix):
    """
    normalizacja macierzy
    """
    matrix = matrix / ((matrix ** 2).sum(axis=0)) ** (1/2)
    return matrix


def apply_maxim(matrix, vector):
    """
    za pomocą wektora vector można określić które kryteria mają być maksymalizowane a które minimalizowane
    """
    # one when maximalize
    # maxims 0 0 1
    v2 = [1 if x == 0 else -1 for x in vector]
    # v2 1 1 -1
    matrix = matrix * v2
    matrix = matrix + vector
    # matrix a b c -> a 1-b 1-c
    return matrix


def apply_weights(matrix, weights):
    """
    zastosowanie wag kryteriów
    """
    return matrix * weights


def get_min(matrix):
    return matrix.min(0)


def get_max(matrix):
    return matrix.max(0)


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


def topsis(matrix, vector, weights):
    """
    cała metoda topsis
    """
    # print(matrix)
    matrix = normalize(matrix)
    # print(matrix)
    matrix = apply_weights(matrix, weights)
    # print(matrix)
    matrix = apply_maxim(matrix, vector)
    # print(matrix)
    min_ = get_min(matrix)
    # print(min_)
    max_ = get_max(matrix)
    # print(max_)
    did = get_did(matrix, max_)
    # print(did)
    dig = get_dig(matrix, min_)
    # print(dig)
    ci = get_ci(dig, did)
    # print(ci)
    rank = sort_res(ci)
    print_rank(rank)


if __name__ == '__main__':
    path = r"D:\ONENOTE\OneDrive\STUDIA\SWD\TOPSIS i ZBIORY ODNIESIENIA\topsis\dane_lapki_do_topsis.csv"
    matrix = import_data(path)
    maxims = 10 * [0]
    maxims[6] = 1
    weights = 10*[1]
    topsis(matrix, maxims, weights)





