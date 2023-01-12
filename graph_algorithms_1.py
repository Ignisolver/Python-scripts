#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import List, Dict
from copy import copy

def adjmat_to_adjlist(adjmat: List[List[int]]) -> Dict[int, List[int]]:
    adj_list = {}
    for row_nr, row in enumerate(adjmat, 1):
        for kol_nr, el in enumerate(row, 1):
            if el != 0:
                if row_nr not in adj_list:
                    adj_list.update({row_nr: []})
                for i in range(el):
                    adj_list[row_nr].append(kol_nr)
    return adj_list


def dfs_recursive(G: Dict[int, List[int]], s: int) -> List[int]:
    visited = []
    _dfs_recursive(G,s,visited)
    return visited

def _dfs_recursive(G: Dict[int, List[int]], v:int, visited: List[int]):
    visited.append(v)
    if v in G:
        for i in G[v]:
            if i not in visited:
                _dfs_recursive(G,i,visited)



def dfs_iterative(G: Dict[int, List[int]], s: int) -> List[int]:
    stack = list(reversed(G[s]))
    visited = [s]
    while len(stack) > 0:
        el = stack.pop()
        if el not in visited:
            visited.append(el)
            if el in G:
                for i in reversed(G[el]):
                    stack.append(i)
    return visited



def is_acyclic(G: Dict[int, List[int]]) -> bool:
    starts = G.keys()
    for start in starts:
        stack = G[start][:]
        while len(stack) > 0:
            el = stack.pop()
            if el == start:
                return False
            else:
                if el in G:
                    for i in G[el]:
                        stack.append(i)
    return True

