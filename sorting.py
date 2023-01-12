from copy import copy


def _quicksort(lista, start: int, stop: int):
    """
    :param lista: lista
    :param start: index pierwszego elementu
    :param stop: index ostatniego elementu
    :return:
    """
    p = start
    k = stop
    pivot = lista[int((p + k) / 2)]
    while p < k:
        while lista[p] < pivot:
            if p == stop:
                break
            p += 1
        while lista[k] > pivot:
            if k == start:
                break
            k -= 1
        if p <= k:
            lista[p], lista[k] = lista[k], lista[p]
            p += 1
            k -= 1
    if start < k:
        _quicksort(lista, start, k)
    if p < stop:
        _quicksort(lista, p, stop)

    return lista


def quicksort(L, start: int = None, stop: int = None):
    start = 0 if start is None else start
    stop = len(L) - 1 if stop is None else stop
    Lis = copy(L)
    _quicksort(Lis, start, stop)
    return Lis


def bubblesort(L):
    lista = copy(L)
    n = len(lista)
    comp_amount = 0
    swap_presence = False

    while n > 1:
        for i in range(1, n):
            comp_amount += 1
            if lista[i - 1] > lista[i]:
                swap_presence = True
                lista[i], lista[i - 1] = lista[i - 1], lista[i]

        if swap_presence:  # optymalizacja w razie wcześnejszego posortowania listy
            swap_presence = False
        else:
            break
        n -= 1
    return lista, comp_amount


# if __name__ == '__main__':
#     print(quicksort([-149, 416, -228, 57, 266, 874, 946, -361, -426, 571, 96, -271, 575, -367, 792, -430, 441, 214, 831, 343, 7, 530, 675, 811,1, 5, 3, 7, 2, 4, 73, 2], 0, 7))
#     print(bubblesort([-149, 416, -228, 57, 266, 874, 946, -361, -426, 571, 96, -271, 575, -367, 792, -430, 441, 214, 831, 343, 7, 530, 675, 811,1, 5, 3, 7, 2, 4, 73, 2]))
#

