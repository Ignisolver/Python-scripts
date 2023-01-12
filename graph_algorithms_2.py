#!/usr/bin/python
# -*- coding: utf-8 -*-
from collections import deque
from math import inf
from typing import List, Set, Dict
from os import getcwd
import networkx as nx

# Pomocnicza definicja podpowiedzi typu reprezentującego etykietę
# wierzchołka (liczba 1..n).
VertexID = int

# Pomocnicza definicja podpowiedzi typu reprezentującego listę sąsiedztwa.
AdjList = Dict[VertexID, List[VertexID]]

Distance = int
B = "biały"
C = "czarny"
S = 'szary'

VertexID = int
EdgeID = int


# Nazwana krotka reprezentująca segment ścieżki.
class TrailSegmentEntry:
    start: VertexID = None
    end: VertexID = None
    id: EdgeID = None
    weight: float = None


Trail = List[TrailSegmentEntry]


def neighbors(adjlist: AdjList, start_vertex_id: VertexID,
              max_distance: Distance) -> Set[VertexID]:
    neighberzy = set()
    kolejka = deque([None, start_vertex_id])
    colors = dict()
    distance = 0
    for key in adjlist:
        colors.update({key: B})
        for el in adjlist[key]:
            colors.update({el: B})
    colors[start_vertex_id] = S
    while len(kolejka) != 0:
        el = kolejka.pop()
        if el is None:
            distance += 1
            kolejka.extendleft([None])
            continue
        if distance == max_distance:
            return neighberzy
        if el in adjlist:
            for sonsiad in adjlist[el]:
                if colors[sonsiad] == B:
                    colors[sonsiad] = S
                    kolejka.extendleft([sonsiad])
                    neighberzy.update([sonsiad])

        colors[el] = C
    return neighberzy


def load_multigraph_from_file(filepath: str) -> nx.MultiDiGraph:
    """Stwórz multigraf na podstawie danych o krawędziach wczytanych z pliku.

    :param filepath: względna ścieżka do pliku (wraz z rozszerzeniem)
    :return: multigraf
    """
    cwd = getcwd()
    edges = []
    g = nx.MultiDiGraph(edges)
    with open(cwd + '\\' + filepath, 'r') as plik:
        for line in plik:
            if line != '\n':
                line = line.strip().split(' ')
                g.add_edge(int(line[0]), int(line[1]), weight=float(line[2]))
    return g


def find_min_trail(g: nx.MultiDiGraph, v_start: VertexID, v_end: VertexID) -> Trail:
    """Znajdź najkrótszą ścieżkę w grafie pomiędzy zadanymi wierzchołkami.

    :param g: graf
    :param v_start: wierzchołek początkowy
    :param v_end: wierzchołek końcowy
    :return: najkrótsza ścieżka
    """
    dijkstra_path_nodes = nx.dijkstra_path(g, v_start, v_end)
    # Na podstawie najkrótszej ścieżki stwórz listę krawędzi tworzących najkrótszą drogę.
    edges_in_path = list(zip(dijkstra_path_nodes[0:], dijkstra_path_nodes[1:]))
    path = []

    for edge in edges_in_path:
        paths = g[edge[0]][edge[1]].items()
        min_path = min(paths, key=lambda x: x[1].get('weight'))
        path_el = TrailSegmentEntry()
        path_el.start = edge[0]
        path_el.end = edge[1]
        path_el.id = min_path[0]
        path_el.weight = min_path[1].get('weight', inf)

        path.append(path_el)
    return path


def trail_to_str(trail: Trail) -> str:
    """Wyznacz reprezentację tekstową ścieżki.

    :param trail: ścieżka
    :return: reprezentacja tekstowa ścieżki
    """
    txt = str(trail[0].start) + ' '
    suma = 0

    for el in trail:
        txt += '-['
        txt += str(el.id) + ': '
        txt += str(el.weight) + ']-> '
        txt += str(el.end) + ' '
        suma += el.weight
    txt += f'(total = {suma})'
    return txt
