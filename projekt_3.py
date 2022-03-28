"""Niech g będzie grafem nieważonym nieskierowanym (obiektem klasy Graph z lab 7).
W grafie odtworzyć nastepującą sieć społecznościową, gdzie postaci oznaczone inicjałami będą wierzchołkami,
a znajomi będą sąsiadami pierwszego stopnia:

VI ma następujących znajomych: CH, RU i PA.
RU ma następujących znajomych: RA, SU i VI.
PA ma następujących znajomych: CO, KE.
CO ma następujących znajomych: RU, VI.

Przygotować funkcję friend_path(g: Graph, f0: Any, f1: Any) -> List[Any], która zwróci wszystkie postaci, którzy stanowią
najkrótsze połączenie pomiędzy postaciami o inicjałach przekazanych w parametrach f0 i f1.

Celem sprawdzenia rozwiązania przygotować 3 dowolne grafy testowe."""

from Graph import *


def friend_path(graph: Graph, f0: Any, f1: Any) -> List[Any]:
    origin = None
    destiny = None
    for vertex in graph.adjacencies:
        if vertex.data == f0:
            origin = vertex
        if vertex.data == f1:
            destiny = vertex

    path = [origin]
    visited = [origin]
    queue = Queue()
    queue.enqueue(path)
    while queue:
        p = queue.dequeue()
        v = p[len(p) - 1]
        for edge in graph.adjacencies[v]:
            if edge.source == v:
                n = edge.destination
            else:
                n = edge.source
            if n not in visited:
                np = []
                np.extend(p)
                np.append(n)
                visited.append(n)
                queue.enqueue(np)
                if n is destiny:
                    return np


g = Graph()

v0 = g.create_vertex("VI")
v1 = g.create_vertex("CH")
v2 = g.create_vertex("RU")
v3 = g.create_vertex("PA")
v4 = g.create_vertex("RA")
v5 = g.create_vertex("SU")
v6 = g.create_vertex("CO")
v7 = g.create_vertex("KE")

g.add_undirected_edge(v0, v1)
g.add_undirected_edge(v0, v2)
g.add_undirected_edge(v0, v3)
g.add_undirected_edge(v2, v4)
g.add_undirected_edge(v2, v5)
g.add_undirected_edge(v2, v0)
g.add_undirected_edge(v3, v6)
g.add_undirected_edge(v3, v7)
g.add_undirected_edge(v6, v2)
g.add_undirected_edge(v6, v0)

g.show()
#
# friend_connection = friend_path(g, "VI", "KE")
# for friend in friend_connection:
#     print(friend.data)

# GRAF TESTOWY 1 (zmodyfikowany graf z lab 7)

g2 = Graph()
vertex0 = g2.create_vertex("LO")
vertex1 = g2.create_vertex("KO")
vertex2 = g2.create_vertex("PO")
vertex3 = g2.create_vertex("CO")
vertex4 = g2.create_vertex("BE")
vertex5 = g2.create_vertex("PE")

g2.add_undirected_edge(vertex0, vertex1)
g2.add_undirected_edge(vertex0, vertex5)
g2.add_undirected_edge(vertex2, vertex1)
g2.add_undirected_edge(vertex2, vertex3)
g2.add_undirected_edge(vertex3, vertex4)
g2.add_undirected_edge(vertex4, vertex1)
g2.add_undirected_edge(vertex4, vertex5)
g2.add_undirected_edge(vertex5, vertex1)
g2.add_undirected_edge(vertex5, vertex2)

# g2.show()
#
# friend_connection2 = friend_path(g2, "LO", "CO")
# for friend in friend_connection2:
#     print(friend.data)

# GRAF TESTOWY 2

g3 = Graph()

fr_0 = g3.create_vertex("TO")
fr_1 = g3.create_vertex("NI")
fr_2 = g3.create_vertex("UN")
fr_3 = g3.create_vertex("IP")
fr_4 = g3.create_vertex("IE")
fr_5 = g3.create_vertex("SO")
fr_6 = g3.create_vertex("TU")
fr_7 = g3.create_vertex("KA")
fr_8 = g3.create_vertex("WE")

g3.add_undirected_edge(fr_0, fr_1)
g3.add_undirected_edge(fr_0, fr_5)
g3.add_undirected_edge(fr_1, fr_2)
g3.add_undirected_edge(fr_2, fr_3)
g3.add_undirected_edge(fr_3, fr_4)
g3.add_undirected_edge(fr_5, fr_6)
g3.add_undirected_edge(fr_6, fr_7)
g3.add_undirected_edge(fr_7, fr_4)
g3.add_undirected_edge(fr_5, fr_8)
g3.add_undirected_edge(fr_8, fr_4)

# g3.show()
#
# friend_connection3 = friend_path(g3, "TO", "IE")
# for friend in friend_connection3:
#     print(friend.data)

# GRAF TESTOWY 3

g4 = Graph()

de = g4.create_vertex("DE")
en = g4.create_vertex("EN")
fr = g4.create_vertex("FR")
pl = g4.create_vertex("PL")
pr = g4.create_vertex("PR")
ru = g4.create_vertex("RU")

g4.add_undirected_edge(en, de)
g4.add_undirected_edge(pl, en)
g4.add_undirected_edge(pr, en)
g4.add_undirected_edge(de, fr)
g4.add_undirected_edge(ru, fr)
g4.add_undirected_edge(pr, ru)

g4.show()

friend_connection4 = friend_path(g4, "PL", "RU")

for friend in friend_connection4:
    print(friend.data)
